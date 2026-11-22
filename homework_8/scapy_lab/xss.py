from __future__ import annotations
import difflib, html, json, re
from dataclasses import dataclass, field
from typing import Iterable, Optional
from urllib.parse import quote, unquote_plus
from .http_analysis import HttpMessage, Param, Transaction, request_parameters

PAYLOADS = ["<script>alert('XSS')</script>", '<img src="nonexistent.jpg" onerror="alert(\'XSS\')">', '"><script>alert(\'XSS\')</script>', "<svg onload=alert('XSS')>", "<script>alert('XSS upload')</script>"]
MARKERS = [(re.compile(r'<\s*script\b', re.I), 'тег <script>'), (re.compile(r'<\s*(?:img|svg|iframe|object|embed)\b', re.I), 'опасный HTML-тег'), (re.compile(r'\bon[a-z]{3,}\s*=', re.I), 'атрибут-обработчик on...='), (re.compile(r'javascript\s*:', re.I), 'псевдопротокол javascript:'), (re.compile(r'\balert\s*\(', re.I), 'вызов alert()'), (re.compile(r'\b(?:confirm|prompt|eval|document\s*\.\s*cookie)\b', re.I), 'опасный JavaScript-код')]


@dataclass
class Injection:
    location: str
    name: str
    value: str
    payloads: list[str] = field(default_factory=list)
    markers: list[str] = field(default_factory=list)

    @property
    def payload(self) -> str:
        return self.payloads[0] if self.payloads else (self.markers[0] if self.markers else '')

    def raw_value(self) -> str:
        return quote(self.value, safe='')


@dataclass
class Reflection:
    payload: str
    reflected: bool
    variant: str = ''
    context: str = ''
    snippet: str = ''
    transaction_index: int = 0


@dataclass
class Finding:
    transaction: Transaction
    injections: list[Injection]
    reflections: list[Reflection]

    @property
    def injected(self) -> bool:
        return any(item.reflected for item in self.reflections)


@dataclass
class Comparison:
    attack: Finding
    baseline: Optional[Transaction]
    same_endpoint: bool
    request_changes: list[str] = field(default_factory=list)
    response_changes: list[str] = field(default_factory=list)
    diff_excerpt: list[str] = field(default_factory=list)


def _variants(value: str) -> list[str]:
    result = [value]
    for _ in range(2):
        decoded = unquote_plus(result[-1])
        if decoded == result[-1]:
            break
        result.append(decoded)
    for item in list(result):
        unescaped = html.unescape(item)
        if unescaped not in result:
            result.append(unescaped)
    return result


def scan_param(param: Param, payloads: Optional[Iterable[str]] = None) -> Optional[Injection]:
    variants = _variants(param.value)
    found_payloads = [payload for payload in (payloads or PAYLOADS) if any(payload in variant for variant in variants)]
    found_markers = [label for regex, label in MARKERS if any(regex.search(variant) for variant in variants)]
    if not found_payloads and not found_markers:
        return None
    return Injection(param.location, param.name, param.value, found_payloads, found_markers)


def scan_request(tx: Transaction, payloads: Optional[Iterable[str]] = None) -> list[Injection]:
    return [injection for param in request_parameters(tx.request) if (injection := scan_param(param, payloads))]


def _classification(payload: str, matched: str, variant: str) -> str:
    if matched != payload:
        return f'экранировано ({variant})'
    if '<script' in payload.lower():
        return 'HTML-тело: внедрён новый тег <script>'
    if re.search(r'<\s*(?:img|svg|iframe|object|embed)\b', payload, re.I):
        return 'HTML-тело: внедрён тег с обработчиком события' if re.search(r'\son[a-z]{3,}\s*=', payload, re.I) else 'HTML-тело: внедрён HTML-тег'
    return 'HTML-тело'


def find_reflections(response: Optional[HttpMessage], payloads: Iterable[str], transaction_index: int = 0) -> list[Reflection]:
    payloads = list(payloads)
    if response is None:
        return [Reflection(payload, False, transaction_index=transaction_index) for payload in payloads]
    text = response.text()
    result = []
    for payload in payloads:
        candidates = [('raw', payload), ('HTML-экранирование', html.escape(payload)), ('HTML-экранирование (<,>)', payload.replace('<', '&lt;').replace('>', '&gt;')), ('URL-кодирование', quote(payload, safe='')), ('JSON-экранирование', json.dumps(payload)[1:-1])]
        found = next(((name, value) for name, value in candidates if value in text), None)
        if found is None:
            result.append(Reflection(payload, False, transaction_index=transaction_index))
            continue
        variant, matched = found
        offset = text.find(matched)
        snippet = re.sub(r'\s+', ' ', text[max(0, offset - 80):offset + len(matched) + 80]).strip()
        result.append(Reflection(payload, True, variant, _classification(payload, matched, variant), snippet, transaction_index))
    return result


def analyze_transactions(transactions: Iterable[Transaction], payloads: Optional[Iterable[str]] = None, link_stored: bool = True, link_window: int = 8) -> list[Finding]:
    txs = list(transactions)
    result = []
    for tx in txs:
        injections = scan_request(tx, payloads)
        if not injections:
            continue
        payload_list = list(dict.fromkeys(payload for injection in injections for payload in injection.payloads))
        reflections = find_reflections(tx.response, payload_list, tx.index)
        if link_stored and payload_list and not any(item.reflected for item in reflections):
            for later in txs:
                if later.index <= tx.index or later.index > tx.index + link_window or later.client != tx.client:
                    continue
                extra = find_reflections(later.response, payload_list, later.index)
                if any(item.reflected for item in extra):
                    reflections.extend(extra)
                    break
        result.append(Finding(tx, injections, reflections))
    return result


def _param_map(tx: Transaction) -> dict[tuple[str, str], str]:
    return {(param.location, param.name): param.value for param in request_parameters(tx.request)}


def _short(value: str, limit: int = 140) -> str:
    value = re.sub(r'\s+', ' ', value)
    return value if len(value) <= limit else value[:limit] + '...'


def build_comparisons(transactions: Iterable[Transaction], findings: Iterable[Finding], payloads: Optional[Iterable[str]] = None) -> list[Comparison]:
    txs = list(transactions)
    catalog = list(payloads or PAYLOADS)
    result = []
    for finding in findings:
        attack = finding.transaction
        normal = [tx for tx in txs if tx.index != attack.index and not scan_request(tx, payloads) and (tx.response is None or not any(payload in tx.response.text() for payload in catalog))]
        same_path = [tx for tx in normal if tx.method == attack.method and tx.path == attack.path]
        before = [tx for tx in same_path if tx.index < attack.index]
        baseline = max(before or same_path, key=lambda tx: tx.index) if same_path else None
        if baseline is None:
            earlier = [tx for tx in normal if tx.index < attack.index]
            baseline = max(earlier, key=lambda tx: tx.index) if earlier else (min(normal, key=lambda tx: tx.index) if normal else None)
        same_endpoint = bool(baseline and baseline.method == attack.method and baseline.path == attack.path)
        changes = []
        if baseline is None:
            changes.append('обычный запрос для сравнения в захвате не найден')
        else:
            if baseline.method != attack.method:
                changes.append(f'метод: {baseline.method} -> {attack.method}')
            if baseline.target != attack.target:
                changes.append(f'URL: {_short(baseline.target, 120)} -> {_short(attack.target, 160)}')
            old_params = _param_map(baseline)
            for injection in finding.injections:
                changes.append(f"{injection.location} '{injection.name}': '{_short(old_params.get((injection.location, injection.name), '<параметр отсутствовал>'), 80)}' -> '{_short(injection.value)}'")
        response_changes = []
        if attack.response is None:
            response_changes.append('ответ сервера в захвате отсутствует')
        elif baseline and baseline.response:
            old, new = baseline.response, attack.response
            response_changes.append(f'статус: {old.status} -> {new.status}')
            response_changes.append(f"Content-Type: '{old.content_type}' -> '{new.content_type}'")
            response_changes.append(f'длина тела (в сети): {old.body_wire_length} -> {new.body_wire_length} байт; после распаковки: {len(old.body_decoded)} -> {len(new.body_decoded)} байт')
        else:
            response_changes.append(f"ответ: статус {attack.response.status}, Content-Type '{attack.response.content_type}', {attack.response.body_wire_length} байт")
        if attack.response and attack.response.content_encoding:
            response_changes.append(f'Content-Encoding: {attack.response.content_encoding}')
        for reflection in finding.reflections:
            if not reflection.reflected:
                response_changes.append('payload в ответе дословно не найден')
                continue
            where = f' [сохранено и отдано в ответе транзакции #{reflection.transaction_index}]' if reflection.transaction_index != attack.index else ''
            response_changes.append(f'payload отражён ({reflection.variant}); контекст: {reflection.context}{where}')
        diff = []
        if same_endpoint and baseline and baseline.response and attack.response:
            diff = [line for line in difflib.unified_diff(baseline.response.text().splitlines(), attack.response.text().splitlines(), fromfile='обычный запрос', tofile='XSS-запрос', lineterm='', n=2) if line.startswith(('+', '-', '@@'))][:24]
        if not diff:
            diff = [f'{item.variant}: {item.snippet}' for item in finding.reflections if item.reflected]
        result.append(Comparison(finding, baseline, same_endpoint, changes, response_changes, diff))
    return result
