clear
clc
% import the data
filename = "csv/Metric_first.csv";
matrix = readmatrix(filename);

% get the matrix size
[num_rows, num_cols] = size(matrix);

% get the median values in columns
mean_values = mean(matrix);

% creating a new graph
figure;

for col = 1:3
    % make binary values
    y = abs(matrix(:, col) - mean_values(col)) > 0.1 * mean_values(col);
    
    % line numbering
    x = 1:num_rows;
    
    % make a binary graph
    plot(x, y, 'o', 'MarkerFaceColor', 'b');
  
  % draw vertical lines
  % stem(x, y, 'Color', 'b', 'Marker', 'none');

    % making a graph not disappearing
    hold on;
end

hold off;

xlabel('Номер строки');
ylabel('Бинарное значение');
title('Бинаризированный график с условием');

% set a limits for y-axis
ylim([-0.5, 1.5]);

% set a marks for y-axis
yticks([0, 1]);
