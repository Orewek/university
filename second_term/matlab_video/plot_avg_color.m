clear
clc
% import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\последняя_минута.xlsx";
matrix = readmatrix(filename);
% get the matrix size
[num_rows, num_cols] = size(matrix);

% creating a new graph
figure;

for col = 1:num_cols
    % values from the columns
    y = matrix(:, col);
    % line numbering
    x = 1:num_rows;
   
    % make a graph for each column
    plot(x, y);
    
    % making a graph not disappearing
    hold on;    
end

hold off;

xlabel('Номер строки');
ylabel('Значение ячейки');
title('График значений матрицы по столбцам');
