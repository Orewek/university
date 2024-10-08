# IEEE 754

```
Вводим число, не целое. Вещественная часть не должна быть < 10^-23 (для 32 бит)
```

### Нормализованный вид
```
нормализованный вид - предстваление числа в виде x * 10^y
1 <= x <= 10; y - действительное число
если число < 0, то и x будет < 0, но в том же интервале по модулю
```
```py
def normal_view(integer: str, frac_part: str) -> str:
    """
    number to a normal view
    """
    int_len_frac_part: int = len(str(int(frac_part)))
    len_frac_part: int = len(frac_part)
    str_len_frac_part: str = str(len_frac_part)
    str_len_integer = str(len(integer))
    con: str = ''
    if abs(int(integer)) >= 1:
        if not (integer.startswith('-')):
            return f'{integer[0]}.{integer[1:]}{frac_part} * 10^{str_len_integer[1:]}'
        return f'{integer[0:2]}.{integer[2:]}{frac_part} * 10^{str_len_integer[1:] - 1}'

    if (integer.startswith('-')):
        con: str = '-'
    if len(str(int(frac_part))) != 1:
        return f'{con}{str_len_frac_part[0]}, {str_len_frac_part[1:]} * 10^(-{str(len_frac_part - int_len_frac_part + 1)})'
    return f'{con}{str_len_frac_part} * 10^(-{str(len_frac_part - int_len_frac_part)})'
```

### Не нормализованный вид
```
Делаем так, чтобы условие 1 <= x <= 10 не выполнялось
```
```py
def non_normal_view(integer: str, frac_part: str) -> str:
    int_len_frac_part: int = len(str(int(frac_part)))
    len_frac_part: int = len(frac_part)
    if abs(int(integer)) >= 1:
        if not (integer.startswith('-')):
            return f'0.{integer}{frac_part} * 10^{str(len(integer))}'
        return f'-0.{integer[1:]}{frac_part} * 10^{str(len(integer) - 1)}'

    if len(frac_part) != int_len_frac_part:
        frac_part: str = frac_part[len_frac_part - int_len_frac_part:]
    if integer == '0':
        return f'0.{frac_part} * 10^{str(len_frac_part - int_len_frac_part)}'
    else:
        return f'-0.{frac_part} * 10^{str(len_frac_part - int_len_frac_part)}'
```

### Перевод вещественной части в двоичный вид
```
Проверяем на несущественные нули, которые в 10-ричной системы не имели бы смысла (00123)
Считаем предстваление по алгоритму:
-умножаем на два
- если > 1, записываем 1 в представление; из числа вычитаем 1
- иначе записываем 0

оьбрасываем нули в конце
```
```py
def to_bin_frac(frac_part: str) -> str:
    """
    to bin frac part
    """
    amount_of_digits: int = 20
    bin_frac: str = ''
    if len(str(int(frac_part))) == len(frac_part):
        frac_part: int = int(frac_part)
        frac_part /= 10**(len(str(frac_part)))
    else:
        zeroes_beginning_frac = len(frac_part) - len(str(int(frac_part)))
        frac_part: int = int(frac_part) / 10**(zeroes_beginning_frac + 1)

    while amount_of_digits:
        frac_part *= 2
        if int(frac_part) >= 1:
            bin_frac += '1'
            frac_part -= 1
        else:
            bin_frac += '0'
        amount_of_digits -= 1
    # deleting zeros at the end
    while bin_frac.endswith('0'):
        bin_frac = bin_frac[:-1]
    return bin_frac
```

#### Считаем мантиссу
```
Проверяем на знак
Считаем экспоненту
Считаем мантиссу числа
Дописывем нули в конце до 32 бит
Представляем в 16-ричной системе
```
```py
# bin to 32bits
number_3e_32bit_bin: str = '1' if number.startswith('-') else '0
number = number.split('.')
# to find out pow(10, exp)
exp: int = len(number[0]) - 1
# pow of exponent
mask: bin = bin(127 + exp)[2:]
number_3e_32bit_bin += f'{"0" * (8 - len(mask))}{mask}'
# remainder of mantissa
number_3e_32bit_bin += (str(number[0]) + str(number[1]))[1:]
# adding zeros to the end
number_3e_32bit_bin: str = number_3e_32bit_bin.ljust(32, '0')
print(f'number into IEEE 32bit: {number_3e_32bit_bin}'
number_3e_32bit_hex: str = ''.join([hex(int(number_3e_32bit_bin[i:i + 4], 2))[2:] for i in range(0, 32, 4)])
```