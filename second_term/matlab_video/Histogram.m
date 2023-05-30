
clear
clc
% import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\FilteredDetections1.csv";
matrix = readmatrix(filename);

% length of vectors from one's
target_length = [3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32];

[num_rows, num_cols] = size(matrix);
% mas for vector count
counts = cell(size(target_length));
for i = 1:length(target_length)
    % initialization of structure for each length
    counts{i} = struct('Length', target_lengths(i), 'Count', 0);
end

for col = 1:num_cols
    % count the sqeuence of one's
    one_sequence = zeros(size(target_length));
    for row = 1:num_rows
        if matrix(row, col) == 1
            for i = 1:length(target_length)
                current_tag_len = target_length(i);
                one_sequence(i) = one_sequence(i) + 1;
                if one_sequence(i) == current_tag_len
                    if row == num_rows || matrix(row + 1, col) == 0
                        counts{i}.Count = counts{i}.Count + 1;
                        % end the count if found a zero
                        one_sequence(i) = 0;
                    end
                elseif one_sequence(i) > current_tag_len
                    % stop counting, if current sequence bigger than desired one
                    one_sequence(i) = 0;
                end
            end
        else
            % stop counting, if found a zero in sequence
            one_sequence = zeros(size(target_length));
        end
    end
end

% mas for values of vectors
length = zeros(size(counts));
% mas for values of counts
count_data = zeros(size(counts));


for i = 1:length(target_length)
    length(i) = counts{i}.Length;
    count_data(i) = counts{i}.Count;
end

% draw a histogram
bar(length, count_data);
xlabel('Длина в кадрах');
ylabel('Количество');
title('Сравнение машин разной длины ');
%{edges = 0:0.2:1; % Границы интервалов

%faceColor = 'g'; % Цвет гистограммы


% Построение гистограммы с настройками
%histogram(data, edges, 'FaceColor', faceColor);
