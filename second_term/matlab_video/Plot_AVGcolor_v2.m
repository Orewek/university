clear
clc
% Import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\последняя_минута.xlsx";
matrix = readmatrix(filename);
[numRows, numCols] = size(matrix); % Получение размеров матрицы

figure; % Создание нового графика

for col = 1:numCols
    y = matrix(:, col); % Значения из столбца
    x = 1:numRows; % Номера строк
    
    plot(x, y); % Построение графика для каждого столбца
    
    hold on; % Удержание текущего графика
    
end

hold off; % Отключение удержания графика

xlabel('Номер строки');
ylabel('Значение ячейки');
title('График значений матрицы по столбцам');