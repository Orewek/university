%{
2
Получаем вектор на вход
Находим сумму компонентов вектора
%}
function symma_vektor = untitled6(vektor, razmernost)
    symma_vektor = 0;
    for i = 1:razmernost
        symma_vektor = symma_vektor + vektor(i);
    end
end

%{
3
-Все элементы матрицы, которые по модулю равны
-минимальному элементу, заменяем на 0
%}
function matrixx = untitled6(matrixx, min_abs)
    for x = 1:3
        for y = 1:3
            if abs(matrixx(x, y)) == min_abs
                matrixx(x, y) = 0;
            end
        end
    end
end