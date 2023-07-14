%{
1
Получаем 4 числа на вход
Функция для первого задания
Если число > 0, меняем знак и * 5
%}
function y = untilted5(a)
    for i = 1:4
        if a(i) > 0
            a(i) = a(i) * (-5);
        end
    end
    disp(a)
end

%{
2
Получаем матрицу на вход
Считаем произведение элементов
%}
function proizvedenie = untilted5(matrixx)
    proizvedenie = 1;
    for x = 1:3
        for y = 1:3
            proizvedenie = proizvedenie * matrixx(x, y);
        end
    end
end

%{
3
Получаем матрицу на вход
Находим минимальное число по модулю
%}
function min_abs = untilted5(matrixx)
    min_abs = 10^10;
    for x = 1:3
        for y = 1:3
            chislo = matrixx(x, y);
            if min_abs > abs(chislo)
                min_abs = abs(chislo);
            end
        end
    end
end

