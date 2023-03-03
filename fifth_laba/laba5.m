clc;
clear;
% Charykov Danila #25

file = fopen("in25.txt", 'r');

% task 1
% amount of letters w/o spaces
%{
head = fscanf(file, '%s', 5);
strlength(head)
%}

% task 2
% We know that the len = 5
% swapping 1st and 5th one
%{
head = fscanf(file, '%d', 5);
type1 = head(1);
type5 = head(5);
head(1) = type5;
head(5) = type1;
head
%}

% task 3
% Making streep (string replace) for each digit
%{
head = fscanf(file, '%s', 5);
head = strrep(head, '1', 'one ');
head = strrep(head, '2', 'two ');
head = strrep(head, '3', 'three ');
head = strrep(head, '4', 'four ');
head = strrep(head, '0', 'zero ');
head
%}

% task 4
% procent_d for digits
%{
head = fscanf(file, '%d', 5);
head
%}

% task 5

%{
file = fopen('Kristina.txt', 'w')
f1 = fprintf(file, '%s', '1 2 3 4 100', [newline '6 7 8 9 0.1 0.2 0.3 0.4 200', ...
            [newline '0.5 0.6 0.7 0.8 300', [newline 'Ларкина Кристина 9061234567']]]);
%}


% task 6
% blue mas % 1 == 0
% green mas % 100 == 0
% orange mas % 0.1 == 0
%{
syms green_mas
syms orange_mas
syms blue_mas
head = fscanf(file, '%d', 5);
for i = 1:5
    if mod(head(i), 100) == 0
        green_mas(length(green_mas) + 1) = head(i);
        head(i)
        green_mas

    else
        blue_mas(i) = head(i);
    end
end

head = fscanf(file, '%g', 9);
for i = 1:9
    if mod(head(i), 100) == 0
        green_mas(length(green_mas) + 1) = head(i);

    elseif mod(head(i), 1) == 0
        blue_mas(i + 4) = head(i);

    else
        orange_mas(i) = head(i);
    end
end

head = fscanf(file, '%g', 5);
for i = 1:5
    head(i);
    if mod(head(i), 100) == 0
        green_mas(length(green_mas) + 1) = head(i);
    else
        orange_mas(i) = head(i);
    end
end

green_mas;
orange_mas;
blue_mas;
%}

fclose(file);

% task 7
%{
x = [1 : 0.1 : 5]
y = sin(25 * x)
plot(y)
%}

% task 8 A
% range(65:122) removing 91:96
% matrix 10 rows 50 cols
% each el random(our_range) and int => str

els = setdiff(65:122, [91, 92, 93, 94, 95, 96]);
matrixx = els(randi(length(els), 10, 50));

matrixx;
%{
char(matrixx)
%}

% task 8 B
% Upper letter in range(65:90)
% replacing this on 35 (#) and count += 1
%{
upper_count = 0;
for i = 1:10
    for j = 1:50
        if  matrixx(i, j) >= 65 && matrixx(i, j) <= 90
            upper_count = upper_count + 1
            matrixx(i, j) = 35;
        end
    end
end
char(matrixx)
%}


% task 8 C
% Creating a table and changing corners
% Between cols making a line
%{
amount_of_cols = 10;
valid_vals = setdiff(65:122, [91, 92, 93, 94, 95, 96]);
matrix = valid_vals( randi(length(valid_vals), 10, 50));
for j = 1:50
    matrix(1, j) = 45;
    matrix(10, j) = 45;
end

for i = 1:10
    matrix(i, 1) = 124;
    matrix(i, 50) = 124;
end

matrix(1, 1) = 43;
matrix(1, 50) = 43;
matrix(10 ,50) = 43;
matrix(10 ,1) = 43;

for i = 1:10
    for j = 1:50
        if mod(j, ceil(50 / amount_of_cols)) == 0
            matrix(i, j) = 124;
            matrix(1, j) = 43;
            matrix(10, j) = 43;
        end
    end
end
char(matrix)
%}

% task 9
% input text, reverse it, while didnt find space, append to result
%{
fprintf('А что вы говорили? ...\n')
text = input('>> ','s');
reversed_text = reverse(text);
result = '';
for x = 1:length(reversed_text)
    if reversed_text(x) == ' '
        break
    end
    result = append(result, reversed_text(x));
end
fprintf('В самом деле, %s?\n', reverse(result))
%}

% task 10
%{
quantifiers = ["все" "несколько" "многие" "некоторые" "каждый" "любые"];
person = ["футболисты" "математики" "боб" "стол" "ребенок" "пальцы" "программисты"];
verbs = ["хотят" "смотрят" "понимают" "читают" "хотят" "боятся" "идут" "играют"];
object = ["крокодил" "апельсин" "пары" "танцев" "вероисповедание" "программирование" "зачет" "МатЛаб"];
fprintf("%s %s %s %s\n", quantifiers(randi(6)), person(randi(7)), verbs(randi(8)), object(randi(8)))
%}

% task 11
% input text, reverse it, change " " to " "; for each step print
%{
text = input('>> ', 's');
reversed_text = reverse(text);
result = '';
for x = 1:length(reversed_text)
    if reversed_text(x) == " "
        reversed_text(x) = "-";
    end
    result = append(result, reversed_text(x));
    fprintf("%s\n", reverse(result))
end
%}

% task 12
% input text, make lower, split, if in split[i] in predlog_soyz += 0; += 1
%{
predlog_soyz = readlines('predlog_soyz.txt');
text = split(lower(input('=> ','s')));
count = 0;
for str = 1:size(text)
    if contains(predlog_soyz, text(str)) == 0
        count = count + 1;
    end
end
fprintf('%d - количество слов в предложении\n', count);
%}

% task 13

countries = readlines('countries.txt');
country = (countries(randi(length(countries))));
answer = country;
country = char(country);
country = country(randperm(length(country)));
fprintf('%s\n', upper(country));

attempts_count = 0;
while attempts_count < 4
    guesser_answer = input('Введите название страны = ','s');
    if guesser_answer == answer
        fprintf('Поздравляю, вы угадали!\n')
        break;
    else
        attempts_count = attempts_count + 1;
        if attempts_count == 4
            fprintf('Неверно, Вы проиграли\nПравильный ответ = %s\n', answer);
            break
        end
        fprintf('Неверно, у вас осталось %d попытки(а)\n', 4 - attempts_count);
    end
end
