for element = 1:30
    %Choosing circle position
    center_x = randi(20); 
    center_y = randi(20);
  
    radius = randi(5);
    %Color of the circle
    color_vektor = rand(1,3);
    
    C = colormap(color_vektor);
    t = 0:pi/1000:2*pi;
    % Drawing the circle
    Y = sin(t) * radius + center_y;
    X = cos(t) * radius + center_x;

    hold on
    plot(X, Y, 'Color', C)
    fill(X, Y, C)
end

axis([-5 25 -5 25])
hold off