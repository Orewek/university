clear
clc
% import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\первая_минута.xlsx";
matrix = readmatrix(filename);

% get the matrix size
[num_rows, num_cols] = size(matrix);

% creating a new graph
figure;

for col = 1:num_cols
    % values from the column
    y = matrix(:, col);
    
    % rows numbering
    x = 1:num_rows;
   
    % making a graph for each column
    plot(x, y);
 
    % making a graph not disappearing
    hold on;
    
end

% get the median values in columns
mean_values = mean(matrix);
for col = 1:num_cols
    % make a binary values
    y = abs(matrix(:, col) - mean_values(col)) > 0.1 * mean_values(col);
    y = 255 * y;

    % rows numbering
    x = 1:num_rows;
    
    % making a binary graph
    plot(x, y, 'o', 'MarkerFaceColor', 'b');
  % draw vercical lines
  % stem(x, y, 'Color', 'b', 'Marker', 'none');
end

hold off;

xlabel('Кадры');
ylabel('Средний цвет');
title('Совмещённый график');
