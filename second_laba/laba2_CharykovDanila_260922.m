%{1%}
%Рандомно задаем число от 3 до 1000
%Оно будет отвечать за размерность вектора
%razmernost = randi([3, 10^3]);
razmernost = 3;
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
%}

%Вектор-строка
vektor;
%Вектор-столбец
vektor';

% Матрица
%for x = 1:2
%    for y = 1:2
%    %chislo = input('element =');

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













        
        





