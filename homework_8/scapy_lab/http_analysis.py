from __future__ import annotations
import gzip, re, zlib
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import parse_qsl, unquote, urlsplit
from scapy.all import IP, IPv6, PcapReader, TCP

PORTS = {80, 8000, 8008, 8080, 8081, 8888}
METHODS = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT'}


@dataclass
class HttpMessage:
    start_line: str
    headers: dict[str, str]
    body: bytes
    body_decoded: bytes
    content_encoding: str = ''
    body_wire_length: int = 0

    @property
    def method(self) -> str:
        return self.start_line.split(' ', 1)[0].upper() if not self.start_line.startswith('HTTP/') else ''

    @property
    def target(self) -> str:
        parts = self.start_line.split(' ')
        return parts[1] if not self.start_line.startswith('HTTP/') and len(parts) > 1 else ''

    @property
    def status(self) -> int:
        try:
            return int(self.start_line.split()[1])
        except (IndexError, ValueError):
            return 0

    @property
    def content_type(self) -> str:
        return self.headers.get('content-type', '').split(';', 1)[0].strip().lower()

    def text(self) -> str:
        try:
            return self.body_decoded.decode('utf-8')
        except UnicodeDecodeError:
            return self.body_decoded.decode('iso-8859-1', 'replace')


def _find_head(data: bytes, pos: int) -> tuple[int, int]:
    a = data.find(b'\r\n\r\n', pos)
    b = data.find(b'\n\n', pos)
    if a < 0:
        return (b, 2) if b >= 0 else (-1, 0)
    if b < 0 or a <= b:
        return a, 4
    return b, 2


def _parse_head(head: bytes) -> tuple[str, dict[str, str]]:
    lines = re.split(r'\r?\n', head.decode('iso-8859-1', 'replace'))
    headers = {}
    for line in lines[1:]:
        if ':' in line:
            name, value = line.split(':', 1)
            headers[name.strip().lower()] = value.strip()
    return (lines[0].strip() if lines else ''), headers


def _decode(body: bytes, headers: dict[str, str]) -> tuple[bytes, str]:
    if not body:
        return b'', ''
    encoding = headers.get('content-encoding', '').strip().lower()
    try:
        if 'gzip' in encoding or (not encoding and body[:2] == b'\x1f\x8b'):
            return gzip.decompress(body), 'gzip'
        if 'deflate' in encoding:
            try:
                return zlib.decompress(body), 'deflate'
            except zlib.error:
                return zlib.decompress(body, -zlib.MAX_WBITS), 'deflate/raw'
    except Exception:
        return body, encoding
    return body, encoding


def parse_http(data: bytes, kind: str) -> list[HttpMessage]:
    out = []
    pos = 0
    while pos < len(data):
        while data[pos:pos + 2] == b'\r\n':
            pos += 2
        while data[pos:pos + 1] == b'\n':
            pos += 1
        head_end, sep = _find_head(data, pos)
        if head_end < 0:
            break
        start_line, headers = _parse_head(data[pos:head_end])
        body_start = head_end + sep
        status = 0
        if kind == 'response':
            try:
                status = int(start_line.split()[1])
            except (IndexError, ValueError):
                status = 0
            if 100 <= status < 200:
                pos = body_start
                continue
        if kind == 'response' and status in (204, 304):
            body, next_pos = b'', body_start
        else:
            raw_length = headers.get('content-length', '')
            if raw_length.isdigit():
                length = int(raw_length)
                body = data[body_start:body_start + length]
                next_pos = body_start + length
            else:
                body = data[body_start:]
                next_pos = len(data)
        decoded, encoding = _decode(body, headers)
        out.append(HttpMessage(start_line, headers, body, decoded, encoding, len(body)))
        pos = next_pos
    return out


@dataclass
class Flow:
    src: str
    sport: int
    dst: str
    dport: int
    segs: list[tuple[int, bytes]] = field(default_factory=list)
    syn: Optional[int] = None
    first: float = 0.0

    def data(self) -> bytes:
        if not self.segs:
            return b''
        base = self.syn + 1 if self.syn is not None else min(seq for seq, _ in self.segs)
        out = bytearray()
        for seq, data in sorted(self.segs):
            offset = seq - base
            if offset < 0:
                data = data[-offset:]
                offset = 0
            if offset > len(out):
                out.extend(b'\0' * (offset - len(out)))
            if offset < len(out):
                data = data[len(out) - offset:]
            out.extend(data)
        return bytes(out)


@dataclass
class CaptureData:
    path: str
    packets: int = 0
    first: float = 0.0
    last: float = 0.0
    flows: dict[tuple[str, int, str, int], Flow] = field(default_factory=dict)

    @property
    def duration(self) -> float:
        return max(0.0, self.last - self.first)


def read_pcap(path: str) -> CaptureData:
    capture = CaptureData(path)
    with PcapReader(path) as reader:
        for number, packet in enumerate(reader, start=1):
            capture.packets = number
            timestamp = float(packet.time)
            capture.first = timestamp if not capture.first else min(capture.first, timestamp)
            capture.last = max(capture.last, timestamp)
            if not packet.haslayer(TCP):
                continue
            if packet.haslayer(IP):
                ip = packet[IP]
            elif packet.haslayer(IPv6):
                ip = packet[IPv6]
            else:
                continue
            tcp = packet[TCP]
            key = (ip.src, int(tcp.sport), ip.dst, int(tcp.dport))
            flow = capture.flows.get(key)
            if flow is None:
                flow = Flow(ip.src, int(tcp.sport), ip.dst, int(tcp.dport), first=timestamp)
                capture.flows[key] = flow
            if int(tcp.flags) & 0x02:
                flow.syn = int(tcp.seq)
            payload = bytes(tcp.payload)
            if payload:
                flow.segs.append((int(tcp.seq), payload))
    return capture


@dataclass
class Transaction:
    index: int
    client: str
    request: Optional[HttpMessage]
    response: Optional[HttpMessage]
    ts: float

    @property
    def method(self) -> str:
        return self.request.method if self.request else '?'

    @property
    def target(self) -> str:
        return self.request.target if self.request else ''

    @property
    def path(self) -> str:
        return urlsplit(self.target).path if self.request else ''

    @property
    def status(self) -> int:
        return self.response.status if self.response else 0


def _looks_request(data: bytes) -> bool:
    head = data.lstrip(b'\r\n \t')[:16]
    return any(head.startswith(method.encode() + b' ') for method in METHODS)


def _looks_response(data: bytes) -> bool:
    return data.lstrip(b'\r\n \t')[:5] == b'HTTP/'


def build_transactions(capture: CaptureData) -> list[Transaction]:
    groups: dict[tuple, list[Flow]] = {}
    for flow in capture.flows.values():
        if not flow.segs:
            continue
        endpoints = tuple(sorted(((flow.src, flow.sport), (flow.dst, flow.dport))))
        groups.setdefault(endpoints, []).append(flow)
    result = []
    for flows in groups.values():
        request_flow = next((f for f in flows if f.dport in PORTS), None)
        response_flow = next((f for f in flows if f is not request_flow), None)
        if request_flow is None:
            for flow in flows:
                data = flow.data()
                if _looks_request(data):
                    request_flow = flow
                elif _looks_response(data):
                    response_flow = flow
        request_data = request_flow.data() if request_flow else b''
        response_data = response_flow.data() if response_flow else b''
        requests = parse_http(request_data, 'request') if request_flow else []
        responses = parse_http(response_data, 'response') if response_flow else []
        for position in range(max(len(requests), len(responses))):
            request = requests[position] if position < len(requests) else None
            response = responses[position] if position < len(responses) else None
            if request is None and response is None:
                continue
            client = request_flow.src if request_flow else response_flow.dst
            timestamp = request_flow.first if request_flow else response_flow.first
            result.append(Transaction(0, client, request, response, timestamp))
    result.sort(key=lambda tx: tx.ts)
    for number, transaction in enumerate(result, start=1):
        transaction.index = number
    return result


@dataclass
class Param:
    location: str
    name: str
    value: str


def _multipart(body: bytes, content_type: str) -> list[tuple[str, str]]:
    match = re.search(r'boundary="?([^";]+)', content_type, re.I)
    if not match:
        return []
    boundary = b'--' + match.group(1).encode('iso-8859-1', 'replace')
    result = []
    for part in body.split(boundary):
        part = part.strip(b'\r\n')
        if not part or part.startswith(b'--'):
            continue
        head, separator, data = part.partition(b'\r\n\r\n')
        if not separator:
            continue
        name = re.search(rb'name="([^"]*)"', head)
        if name:
            result.append((name.group(1).decode('utf-8', 'replace'), data.rstrip(b'\r\n').decode('utf-8', 'replace')))
    return result


def request_parameters(request: Optional[HttpMessage]) -> list[Param]:
    if request is None:
        return []
    split = urlsplit(request.target)
    params = [Param('path', 'PATH', unquote(split.path))]
    params.extend(Param('query', name, value) for name, value in parse_qsl(split.query, keep_blank_values=True))
    body = request.body_decoded or request.body
    if not body:
        return params
    content_type = request.content_type
    if content_type == 'application/x-www-form-urlencoded':
        params.extend(Param('body', name, value) for name, value in parse_qsl(body.decode('utf-8', 'replace'), keep_blank_values=True))
    elif content_type == 'multipart/form-data':
        params.extend(Param('body', name, value) for name, value in _multipart(body, request.headers.get('content-type', '')))
    else:
        params.append(Param('body', '(raw body)', body.decode('utf-8', 'replace')))
    return params
