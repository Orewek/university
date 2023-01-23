% Charykov Danila #25 task 5
hold on
axis([-0.2 1 -0.2 1])
amount_of_els = 10;
while amount_of_els > 0
  % Случайно задаем цвет
  c = rand(1, 3);
  C = colormap(c);
  x = rand(1, 4);
  y = rand(1, 4);
  x(4) = x(1);
  y(4) = y(1);
  l = [0 0 0];
  for j = 1:3
    % Считаем длину ребра
    l(j) = sqrt((x(j) - x(j + 1))^2 + (y(j) - y(j + 1))^2);  
  end
  epsilon = 0.01;
  % Проверяем что все стороны отличаются не более чем на эпсилон
  if and((abs(l(3) - l(1)) < epsilon), and((abs(l(2) - l(1)) < epsilon), (abs(l(2) - l(3)) < epsilon)))
    line(x, y)
    fill(x, y, C)
    amount_of_els = amount_of_els - 1;
  end
end