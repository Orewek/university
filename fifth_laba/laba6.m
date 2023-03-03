% task 1
%{
n = input('Введите число от 1 до 4: ');
r = 255*rand(1,1);
switch n
   case 1
       A = [r, r, r+101, r+99, r+120; r, r, r+121, r+115, r+107; r, r, r+111, r+110, r+102; r, r, r, r, r; r, r, r, r, r];
     
   case 2
       A = [r+53, r+42, r+33, r, r; r+74, r+55, r+46, r, r; r+67, r+58, r+24, r, r; r, r, r, r, r; r, r, r, r, r];
   case 3
       A = [ r, r, r, r, r; r, r, r, r, r; r+74, r+55, r+46, r, r;  r+67, r+58, r+24, r, r; r+53, r+42, r+33, r, r];
   otherwise
       A = [ r, r, r, r, r;  r, r, r, r, r; r, r, r+101, r+99, r+120;  r, r, r+121, r+115, r+107; r, r, r+111, r+110, r+102;];
      
end 
       image(A)
       colorbar
%}

% task 2
%{
d = imread("democracy.png");
subplot(2,2,1)
imhist(d(:,:,1))
title("Гистограмма Красного")
subplot(2,2,2)
imhist(d(:,:,2))
title("Гистограмма Зелёного")
subplot(2,2,3)
imhist(d(:,:,3))
title("Гистограмма Синего")
r = d(:,:,1);
g = d(:,:,2);
b = d(:,:,3);
red = imhist(r);
green = imhist(g);
blue = imhist(b);
subplot(2,2,4)
x = 0:255;
hold on
plot(x,red,'r')
plot(x,green,'g')
plot(x,blue,'b')
%}

% task 3
%{
d = imread("democracy.png");
a = imread("democracy.png");
subplot(1,2,1)
image(d);
subplot(1,2,2)
k = randi([0 300],1,5);
for i = 1:2:3
   a(:,:,i) = k(randi(5));
end
image(a);
%}

% task 4
%{
d = imread("democracy.png");
a = imread("democracy.png");
subplot(1,2,1)
image(d);
subplot(1,2,2)
for i = 1:3
   a(:,:,i) = a(:,:,i)+80;
end
image(a);
%}

% task 5
%{
d = imread("democracy.png");
subplot(2,2,1)
image(d)
r=cvet(d,string("R"));
subplot(2,2,2)
image(r)
g=cvet(d,string("G"));
subplot(2,2,3)
image(g)
b=cvet(d,string("B"));
subplot(2,2,4)
image(b)
%}

% task 6
%{
d = imread('democracy.png');
count = 0;
       while count < 30
       x = randi([30;900]);
       y_vverx = randi([100;400]);
       y_nizhn = randi([700;1200]);
         for i = y_vverx:y_nizhn
           d(i,x,:) = 200;
         end
         count = count + 1;
       end
RedChannel = d(:,:,1);
GreenChannel = d(:,:,2);
BlueChannel = d(:,:,3);
outputRed = (RedChannel *.393) + (GreenChannel *.769) + (BlueChannel *.189);
outputGreen = (RedChannel *.349) + (GreenChannel *.686) + (BlueChannel *.168);
outputBlue = (RedChannel *.272) + (GreenChannel *.534) + (BlueChannel *.131);
out = uint8(cat(3, outputRed, outputGreen, outputBlue));
  
figure;
imshow(out);
%}

% task 7
%{
d = imread("democracy.png");
d = rgb2gray(d);
for k= 2:2:8
   len=size(d)/k;
   for i = 1:len(1);
       for j = 1:len(2);
       d(i,j)= d(i*k,j*k);
       end
   end
end
imshow(d)
%}

% task 8
%{
d = imread("democracy.png");
image(d)
r=rand(1,3);
%subplot(2)
k=ramka(d,60,r);
subplot(2,2,1)
image(k);
k = ramka(d,100,rand(1,3));
subplot(2,2,2)
image(k);
k = ramka(d,17,rand(1,3));
subplot(2,2,3)
image(k);
%}

% task 9
d = imread("democracy.png");
m = 10;
n = 10;
k = shuffle_image(d,m,n);
image(k);





