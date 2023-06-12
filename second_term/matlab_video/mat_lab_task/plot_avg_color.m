clear
clc
% import the data
filename = "csv_2/Metric_last.csv";
matrix = readmatrix(filename);
% get the matrix size
[num_rows, num_cols] = size(matrix);

% creating a new graph
figure;

for col = 60
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
