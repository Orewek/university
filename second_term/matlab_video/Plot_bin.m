
clear
clc
% Import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\первая_минута.xlsx";
matrix = readmatrix(filename);
[numRows, numCols] = size(matrix); % Получение размеров матрицы

meanValues = mean(matrix); % Вычисление средних значений по столбцам

figure; % Создание нового графика

for col = 1:numCols
    y = abs(matrix(:, col) - meanValues(col)) > 0.1 * meanValues(col); % Бинаризация значений
    
    x = 1:numRows; % Номера строк
    
    plot(x, y, 'o', 'MarkerFaceColor', 'b'); % Построение бинаризированного графика
  %  stem(x, y, 'Color', 'b', 'Marker', 'none'); % Отображение вертикальных линий
    hold on; % Удержание текущего графика
end

hold off; % Отключение удержания графика

xlabel('Номер строки');
ylabel('Бинарное значение');
title('Бинаризированный график с условием');

ylim([-0.5, 1.5]); % Установка пределов для оси y

yticks([0, 1]); % Установка отметок на оси y