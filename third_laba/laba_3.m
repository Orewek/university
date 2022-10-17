%Делал задание 10, т.к. не было 25

%{
1
Вводим с клавиатуры 4 числа
Если число > 0, меняем знак и * 5
%}
for i = 1:4
    number = input('Input the number ');
    a(i) = number;
end
untilted5(a)

%{
2
Создаем случайный массив (0; 10)
Считаем произведение элементов
Создаем вектор по заданной формуле
Считаем сумму его компонентов
Считаем вектор С, по заданной формуле
%}
razmernost = 3;
syms matrixx;
for x = 1:razmernost
    for y = 1:razmernost
        chislo = randi([10]);
        matrixx(x, y) = chislo;
    end
end

matrixx;
proizvedenie = untilted5(matrixx);

syms vektor;
for i = 1:3
    vektor(i) = i * sin(i) * log(i);
end

symma_vektor = untitled6(vektor, razmernost);

vektor;
symma_vektor;

C = proizvedenie * symma_vektor * matrixx * vektor'

%{
3
Создаем случайный массив
Находим в нем минимальное значение по модулю
-Все элементы, которые по модулю равны с минимальным
-заменяем на 0
%}
razmernost = 3;
syms matrixx;
min_abs = 10^10;

for x = 1:razmernost
    for y = 1:razmernost
        chislo = randi([-10^3, 10^3]);
        matrixx(x, y) = chislo;
    end
end
matrixx;
min_abs = untilted5(matrixx);
matrixx = untitled6(matrixx, min_abs);
