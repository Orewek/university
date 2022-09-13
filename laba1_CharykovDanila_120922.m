%{Charykov Danila #25}%

%{3}%
sin(pi / 7) ^ 2 + cos(pi / 7) ^ 2;
sin(pi / 182) ^ 2 + cos(pi / 182) ^ 2;
sin(22) ^ 2 + cos(22) ^ 2;

%{4}%
x = 2.5;
b = 0.04;
k = 3;
n = 5;

y = 1/9 - 10 ^ -4 * (exp(k * x)) + cos(sqrt(x ^ 2 + b)) + (sqrt(x ^ 2 + b) / (0.4 * x)) + (sin(3) / ((x ^ 2 + b) * n));

%{5}%
nchoosek(13, 4);
nchoosek(10, 5);

%{6}%
x = 552;
log(exp(x)) == x;

%{7}%

%{8}%
syms x
res = solve(0.5 * ((x - 2) ^ 3) - 40 * sin(x) == 0)