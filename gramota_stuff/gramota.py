def main(number: str) -> str:
    """
    znak: проверка на знак;
    - (1: < 0 ; 0: >= 0)

    exp_stepen: Экпонициальная степень
    - Разделяем число на целую и дробную часть
    - Считаем длину целой части - 1; len(100) - 1 = 2
    - Прибавляем 127, чтобы число получилось положительным (для записи в память)
    - Переводим из 10 в 2 степень

    change_dec_point: Мантисса
    - Делим число на (10 ** exp_stepen)
    - Получается число вида x.yzki...l
    - Оставляем дробную часть

    res: Число в 2 системе
    - Складываем все кусочки в единое целое
    - Если длина < 32 => дописываем слева нули

    hes_res: Число в 16 системе
    - Делим на кусочки по 4 цифры
    - Переводим каждой кусочек в 16 систему
    - Складываем получившиеся кусочки
    """
    znak = 1 if number.startswith('-') else 0
    exp_stepen = bin(len(number.replace('-', '').split('.')[0]) - 1 + 127)[2:]
    change_dec_point = number.replace('-', '').replace('.', '')[1:]

    res = f'{znak}{exp_stepen}{change_dec_point}'.ljust(32, '0')
    hex_res = ''.join([hex(int(res[i:i + 4], 2))[2:] for i in range(0, 32, 4)])

    return hex_res


if __name__ == '__main__':
    print('Input bin number')
    number = input()
    bit32 = main(number)
    print(bit32)
