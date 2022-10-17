%{1%}
%Рандомно задаем число от 3 до 1000
%Оно будет отвечать за размерность вектора
%Чтобы продемонстрировать работу программы, будем использовать 5-мерный
%razmernost = randi([3, 10^3]);
razmernost = 5;
syms vektor;

%Создадим вектор
%В каждый аргумент рандомно
%будет записываться число от -1000 до 1000
for i = 1:razmernost
    chislo = randi([-10^3, 10^3]);
    vektor(i) = chislo;
end

%Передадим вектор в упорядочный вектор
% Функция  O(n^2), пузырьком
% По условию сравнение модулей чисел
vektor_ypor = vektor;
for dx = 1:razmernost
    for x = 1:razmernost - 1
        if abs(vektor_ypor(x)) < abs(vektor_ypor(x + 1))
            type_x = vektor_ypor(x);
            vektor_ypor(x) = vektor_ypor(x + 1);
            vektor_ypor(x + 1) = type_x;
        end
    end
end

%Найдем сумму всех аргументов вектора
symma = 0;
for x = 1:razmernost
    symma = symma + vektor_ypor(x);
end


%К последнему элементу исходного вектора
% прибавим получившуюся сумму
vektor(razmernost) = vektor(razmernost) + symma;

%{
%2
%Задаем вектор-строку с клавиатуры

syms vektor
for i = 1:2
    chislo = input('element =');
    vektor(i) = chislo;
end

% Матрица
for x = 1:2
    for y = 1:2
    chislo = input('element =');
    matrix([x],[y]) = chislo;
    end
end

%Вектор-строка
vektor
%Вектор-столбец
vektor'
%Матрица
matrix
%}
%3
matrix_dot = zeros(2);
matrix1 = ones(2);
matrix_mr = randi([-10^3, 10^3], 2);

diagonal = [1 1];
diag(diagonal);

%4

Matrix = matrix_dot * matrix_mr - 100;

%5
%shape matrix
max(max(Matrix));
min(min(Matrix));
sum(sum(Matrix));

peremnoj = 1;
for y = 1:2
    for x = 1:2
        peremnoj = peremnoj * Matrix(x, y);
    end
end
peremnoj;

%6 7 8 9 10
% Так как 25 варианта нет, взял 24
A = [0.1525 -0.4035 -0.0799 -0.7312;
    -0.5043 0.2772 -0.9274 -0.0132;
    0.1472 0.6316 -0.3821 -0.5334;
    0.5896 0.1167 1.5805 1.6554;
    0.3078 -0.1118 -0.7713 -1.2083;
    -0.5862 -0.0282 0.1948 -1.1212];

B = [0.05 0.0784 0.0046 0.29;
    0.575 0.0064 0.698 0.543;
    0.4567 0.002 0.578 0.445;
    0.0446 0.268 0.077 0.0057];

C = [0.0063 0.038 0.67 0.0054;
    0.57 0.05 0.0784 0.0046;
    0.0044 0.575 0.0064 0.698;
    0.997 0.4567 0.002 0.578];

% A не содержит B, поэтому создаем B1 той же размерности
% Умножаем матрицы, делим и транспонируем
B1 = A([1:3], [1:4]);
B1*C;
B1/C;
A';
