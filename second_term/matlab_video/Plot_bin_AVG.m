
clear
clc
% Import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\первая_минута.xlsx";
matrix = readmatrix(filename);
[numRows, numCols] = size(matrix); % Получение размеров матрицы

figure; % Создание нового графика

for col = 1:numCols
    y = matrix(:, col); % Значения из столбца
    x = 1:numRows; % Номера строк
    
    plot(x, y); % Построение графика для каждого столбца
    
    hold on; % Удержание текущего графика
    
end
meanValues = mean(matrix); % Вычисление средних значений по столбцам
for col = 1:numCols
    y = abs(matrix(:, col) - meanValues(col)) > 0.1 * meanValues(col); % Бинаризация значений
    y=255*y;
    x = 1:numRows; % Номера строк
    
    plot(x, y, 'o', 'MarkerFaceColor', 'b'); % Построение бинаризированного графика
  %  stem(x, y, 'Color', 'b', 'Marker', 'none'); % Отображение вертикальных линий
end
hold off; % Отключение удержания графика

xlabel('Кадры');
ylabel('Средний цвет');
title('Совмещённый график');