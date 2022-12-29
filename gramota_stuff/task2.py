def normal(q:str, w:str):  # преобразует число в нормаллизованный вид
    if abs(int(q)) >= 1:  # целая часть числа больше или равна 1
        if q[0] != '-':
            return q[0] + '.' +q[1:] + w + '*10^' + str(len(q[1:]))
        return q[0:2] + '.' +q[2:] + w + '*10^' + str(len(q[1:])-1)
    else:
        if len(str(int(w))) != 1:  # если дробная часть числа по длине равна не 1
            if q[0] != '-':
                return str(int(w))[0] + ',' + str(int(w))[1:] + '*10^(-' + str(len(w) - len(str(int(w)))+1)+')'
            return '-' + str(int(w))[0] + ',' + str(int(w))[1:] + '*10^(-' + str(len(w) - len(str(int(w)))+1)+')'
        else:
            if q[0] != '-':
                return str(int(w)) + '*10^(-' + str(len(w) - len(str(int(w)))+1)+')'
            return '-' + str(int(w))+'*10^(-' + str(len(w) - len(str(int(w))))+')'


def unnormal(q: str, w: str):
    if abs(int(q)) >= 1:  # если число по модулю больше 1
        if q[0] != '-':
            return '0.' + q + w + '*10^' + str(len(q))
        return '-0.' + q[1:] + w + '*10^' + str(len(q) - 1)
    else:  # число по модулю меньше 1
        if q == '0':  # если число не отрицательное
            print('число по модулю меньше 1 и положительное')
            if len(w) != len(str(int(w))):  # есть нули после запятой
                return '0.' + w[len(w) - len(str(int(w))):] + '*10^(-' + str(len(w) - len(str(int(w))))+')'
            else:
                return '0.' + w + '*10^' + str(len(w) - len(str(int(w))))
        else:
            if len(w) != len(str(int(w))):
                return '-0.' + w[len(w) - len(str(int(w))):] + '*10^(-' + str(len(w) - len(str(int(w))))+')'
            else:
                return '-0.'+ w + '*10^' + str(len(w) - len(str(int(w))))


def to_bin(w):  # перевод в двоичную систему числа после точки
    count = 20  # значение будет вычислено вплоть до 14 знаков
    h = ''  # сюда будет записано двоичное представление
    if len(str(int(w))) == len(w):
        w = int(w)
        w /= 10**(len(str(w)))
    else:
        z_co = len(w) - len(str(int(w)))
        w = int(w) /10**(z_co+1)
    while count:
        w *= 2
        if w >= 1:
            h = h + '1'
            w -= 1
        else:
            h = h + '0'
        count -= 1
    while True:  # удаляются лишние нули
        if h[-1] == '0':
            h = h[:-1]
        else:
            break
    return h
while True:
    try:
        a,b = [str(i) for i in input('Введите десятичное число c точкой такое, что его десятичная часть отлична от 0 ').split('.')]
        if int(a) != 0:  # если число по модулю меньше единицы
            if a[0] == '-':
                x = '-' + str(bin(int(a))[3:] + '.' + to_bin(b))
            else:
                x = str(bin(int(a))[2:] + '.' + to_bin(b))
        else:
            if a[0] == '-':
                x = '-0' + '.' + to_bin(b)
            else:
                x = '0'+ '.' + to_bin(b)

        print('Нормализованный вид числа: ', normal(a,b))
        print('Ненормализованный вид числа: ', unnormal(a,b))

        #код ниже переводит двоичную запись числа с точкой в 32битный вид
        s = ''
        if x[0] == '-':
            s = s + '1'
        else:
            s = s + '0'
        x = x.split('.')  # нужно к этому шагу приести число к двоичному виду с точкой
        print(x)
        delta = len(x[0]) - 1  # для определении степени числа
        s = s + '0'*(8-len(bin(127+delta)[2:])) + bin(127+delta)[2:]  # запись степени экспоненты
        s = s + (str(x[0])+str(x[1]))[1:]  # запись остатка от мантиссы
        s = s + '0' * (32-len(s))  # приписывание нулей
        print('Запись числа в формате IEEE 32bit: ',s)
        i = 0
        ss = ''

        while i < 32:  # перевод в 16 с/с
            ss = ss + hex(int(s[i:i+4],2))[2:]
            i += 4
        print('Шестнадцатиричное представление числа в 32битной записи: ', ss)
    except:
        print('Ошибка ввода(!) / Число невозможно перевести, так как его десятичная часть очень мала по модулю')