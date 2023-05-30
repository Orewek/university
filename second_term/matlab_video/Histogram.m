
clear
clc
% Import the data
filename = "C:\Users\User\Desktop\Даннные в Метрики 1\FilteredDetections1.csv";
matrix = readmatrix(filename);

targetLengths = [3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]; % Желаемые длины векторов из единиц

[numRows, numCols] = size(matrix);
counts = cell(size(targetLengths)); % Ячейковый массив для хранения счетчиков количества векторов
for i = 1:length(targetLengths)
    counts{i} = struct('Length', targetLengths(i), 'Count', 0); % Инициализация структуры для каждой длины
end

for col = 1:numCols
    currentCounts = zeros(size(targetLengths)); % Счетчики текущего количества подряд идущих единиц для каждой длины
    for row = 1:numRows
        if matrix(row, col) == 1
            for i = 1:length(targetLengths)
                targetLength = targetLengths(i);
                currentCounts(i) = currentCounts(i) + 1;
                if currentCounts(i) == targetLength
                    if row == numRows || matrix(row+1, col) == 0
                        counts{i}.Count = counts{i}.Count + 1;
                        currentCounts(i) = 0; % Сбросить счетчик после учета последовательности
                    end
                elseif currentCounts(i) > targetLength
                    currentCounts(i) = 0; % Сбросить счетчик, если текущая последовательность длиннее искомой
                end
            end
        else
            currentCounts = zeros(size(targetLengths)); % Сбросить счетчики, если встречается 0
        end
    end
end

lengths = zeros(size(counts)); % Массив для хранения значений длин векторов
countsData = zeros(size(counts)); % Массив для хранения значений счетчиков

for i = 1:length(targetLengths)
    lengths(i) = counts{i}.Length;
    countsData(i) = counts{i}.Count;
end

bar(lengths, countsData); % Построение гистограммы
xlabel('Длина в кадрах');
ylabel('Количество');
title('Сравнение машин разной длины ');
%{edges = 0:0.2:1; % Границы интервалов

%faceColor = 'g'; % Цвет гистограммы


% Построение гистограммы с настройками
%histogram(data, edges, 'FaceColor', faceColor);
