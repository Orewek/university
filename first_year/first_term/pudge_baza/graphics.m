grid on

x = linspace(0, 3.14, 100);
y = sin(x);
a = [1:100];

%plot(x, y.*a);

t = linspace(0, 50, 100)
x = t .* cos(t);
y = t .* sin(t);

hold on
% hold off
%polar(t, x)
%polar(t, y)
%polar(t, sin(4 * t))
p = 0.5;
%comet(x, y, p)
%bar(x);
%hist(x);
hold off
%plot3(x, y, t);
[X, Y] = meshgrid([-3:0.25:3], [-3:0.25:3]);
Z = sin(X) .* sin(Y);


colormap(bone)
shading flat
subplot(2, 3, 1);
mesh(X, Y, Z);
title('Pidger')
xlabel('Chin chopa Hook Shopa')
ylabel('Dobryak Duf')
zlabel('Pudge s basherom')

subplot(2, 3, 5);
surf(X, Y, Z);
title('Bucher')
xlabel('Buchka')
ylabel('Rudge')
zlabel('Paidger')

subplot(2, 3, 3);
surfl(X, Y, Z);
title('Al Padgino')
xlabel('Hooker')
ylabel('Pidgak')
zlabel('Pudge s momom')

alpha(0)
view(45, 45)


%{
u = linspace(0, 2 * pi, 40);
v = linspace(0, 2 * pi, 20);
[U, V] = meshgrid(u, v);

x = (5 + 2 * cos(V)) .* cos(U);
y = (5 + 2 * cos(V)) .* sin(U);
z = 2 .* sin(V);

surf(x, y, z)
axis([-10 10 -10 10 -10 10])
%}

%{
u = linspace(0, 2 * pi, 50);
v = linspace(-0.1, 0.1, 50);
[U, V] = meshgrid(u, v);

x = cos(U) + V .* cos(U / 2) .* cos(U);
y = sin(U) + V .* cos(U / 2) .* sin(U);
z = V * sin(U / 2);

surf(x, y, z)
%}

%{
hold on
a = 10; b = 10;
u = linspace(0, pi, 50);
v = linspace(0, 2 * pi, 50);
[U, V] = meshgrid(u, v);
r = 1 - cos(U ./ 2);

x = a .* cos(U) .* (1 + sin(U)) + r .* cos(U) .* cos(V);
y = b .* sin(U) + r .* sin(U) .* cos(V);
z = r .* sin(V);

surf(x, y, z)

u = linspace(0, 2 * pi, 50);
v = linspace(0, 2 * pi, 50);
[U, V] = meshgrid(u, v);
r = 1 - cos(U ./ 2);

x = a .* cos(U) .* (1 + sin(U)) + r .* cos(V + pi);
y = b .* sin(U);
z = r .* sin(V);

surf(x, y, z)
%}



