 shading flat
syms Xvektor;
syms Yvektor;

for x = 1:10
    Xvektor(x) = x;
    Yvektor(x) = x * sin(x);
end

subplot(2, 3, 1);
plot(Xvektor, Yvektor);
title('x * sin(x)')

for x = 1:10
    Xvektor(x) = x;
    Yvektor(x) = x + sin(x);
end

subplot(2, 3, 2);
plot(Xvektor, Yvektor);
title('x + sin(x)')

for x = 1:10
    Xvektor(x) = x;
    Yvektor(x) = exp(x) + sin(x);
end

subplot(2, 3, 3);
plot(Xvektor, Yvektor);
title('e^x + sin(x)')

%Generated
x_generated = linspace(0, 10);
f1 = x_generated .* sin(x_generated);
f2 = x_generated + sin(x_generated);
f3 = exp(x_generated) + sin(x_generated);

subplot(2, 3, 4);2
plot(x_generated, f1);
title('x * sin(x)')

subplot(2, 3, 5);
plot(x_generated, f2);
title('x + sin(x)')

subplot(2, 3, 6);
plot(x_generated, f3);
title('e^x + sin(x)')
