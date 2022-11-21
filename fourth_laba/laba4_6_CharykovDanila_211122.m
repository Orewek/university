% Charykov Danila #25 task 
green = 31;
blue = 25;
red = 0;
for i = 1:7 %кол-во ёлок
% Первый - красный; Второй - зеленый; Третий - синий
c = [red/255 green/255 blue/255];
C = colormap(c);

x = [0:2:18; 0 1:2:17];
y = [20:-2:1; 20:-2:1]*3;
x = [-fliplr(x(:)') x(:)'];
y = [fliplr(y(:)') y(:)'];

for j = 1:length(x)
    x(j) = x(j) + 5 * (7 + i);
end
for k = 1:length(y)
    y(k) = y(k) - 2 * (7 + i);
end
% Увеличиваем "яркость" зеленого, становится светлее
green = green + 32;
blue = blue - 3;
hold on
axis equal off
fill(x.*i, y.*i, C)
end