def normal_view(integer: str, frac_part: str) -> str:
    """
    number to a normal view
    """
    if abs(int(integer)) >= 1:
        if not (integer.startswith('-')):
            return f'{integer[0]}.{integer[1:]}{frac_part} * 10^{str(len(integer[1:]))}'
        return f'{integer[0:2]}.{integer[2:]}{frac_part} * 10^{str(len(integer[1:]) - 1)}'
    else:
        if not (integer.startswith('-')):
            negative = '-'
        else:
            negative = ''
        if len(str(int(frac_part))) != 1:
            return f'{negative}{str(int(frac_part))[0]}, {str(int(frac_part))[1:]} * 10^-({str(len(frac_part) - len((str(int(frac_part))) + 1))})'
        else:
            return f'{negative}{str(int(frac_part))} * 10^(-{str(len(frac_part) - len(str(int(frac_part))))})'


def non_normal_view(integer: str, frac_part: str) -> str:
    if abs(int(integer)) >= 1:
        if not (integer.startswith('-')):
            return f'0.{integer}{frac_part} * 10^{str(len(integer))}'
        return f'-0.{integer[1:]}{frac_part} * 10^{str(len(integer) - 1)}'
    else:
        if len(frac_part) != len(str(int(frac_part))):
                frac_part = frac_part[len(frac_part) - len(str(int(frac_part))):]
        if integer == '0':
            return f'0.{frac_part} * 10^{str(len(frac_part) - len(str(int(frac_part))))}'
        else:
            return f'-0.{frac_part} * 10^{str(len(frac_part) - len(str(int(frac_part))))}'


def to_bin_frac(frac_part: str) -> str:
    """
    to bin frac part
    """
    amount_of_digits = 20  # how many digits
    bin_frac = ''
    if len(str(int(frac_part))) == len(frac_part):
        frac_part = int(frac_part)
        frac_part /= 10**(len(str(frac_part)))
    else:
        zeroes_beginning_frac = len(frac_part) - len(str(int(frac_part)))
        frac_part = int(frac_part) / 10**(zeroes_beginning_frac + 1)

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


def main() -> None:
    try:
        print('Input a number % 1 != 0\n')
        number = input()
        # number = '-10.1'
        integer, frac_part = number.split('.')

        if integer.startswith('-'):
            negative = '-'
        else:
            negative = ''

        if int(integer) != 0:
            number = negative + str(bin(int(integer))[2:] + '.' + to_bin_frac(frac_part))
        else:
            number = f'{negative}0.{to_bin_frac(integer)}'

        print(f'normalized view: {normal_view(integer, frac_part)}')
        print(f'non-normalized view: {non_normal_view(integer, frac_part)}')

        # bin to 32bits
        number_3e_32bit_bin = ''
        if number.startswith('-'):
            number_3e_32bit_bin += '1'
        else:
            number_3e_32bit_bin += '0'

        number = number.split('.')
        # to find out pow(10, exp)
        exp = len(number[0]) - 1
        # pow of exponent
        number_3e_32bit_bin += '0' * (8 - len(bin(127 + exp)[2:])) + bin(127 + exp)[2:]
        # remainder of mantissa
        number_3e_32bit_bin += (str(number[0]) + str(number[1]))[1:]
        # adding zeros to the end
        number_3e_32bit_bin = number_3e_32bit_bin.ljust(32, '0')
        print(f'number into IEEE 32bit: {number_3e_32bit_bin}')

        number_3e_32bit_hex = ''.join([hex(int(number_3e_32bit_bin[i:i + 4], 2))[2:] for i in range(0, 32, 4)])
        print(f'hex in 32bits: {number_3e_32bit_hex}')
    except:
        print('Error! number is an integer or fractional part is tooo small')


if __name__ == '__main__':
    main()
