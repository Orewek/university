function y = cvet(im,col)
if col == string("R")
im(:,:,1) =randi(300);
y = im;
end
if col == string("G")
im(:,:,2)= randi(300);
y = im;
end
if col == string("B")
im(:,:,3)= randi(300);
y = im;
end
