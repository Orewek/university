%Charykov Danila #25 (11)
shading flat
syms Xvektor;
syms Yvektor;

range_x = 100;

for x = -(range_x):range_x
    if x <= -1
        Xvektor(abs(x)) = x;
        Yvektor(abs(x)) = (1 + abs(x)) / ((1 + x + x^2)^(1/3));
    end
    if x > -1
        Xvektor(abs(x) + 2) = x;
        Yvektor(abs(x) + 2) = (1 + cos(x)^4) / (x + 3);
    end
end

subplot(1, 2, 1);
plot(Xvektor, Yvektor);

hold on
x_generated = linspace(-range_x, -1);
f1 = (1 + abs(x_generated)) ./ ((1 + x_generated + x_generated.^2).^(1/3));

subplot(1, 2, 2);
plot(x_generated, f1);

x_generated = linspace(-1, range_x);
f2 = (1 + cos(x_generated).^4) ./ (x_generated + 3);



subplot(1, 2, 2);
plot(x_generated, f2);
hold off


