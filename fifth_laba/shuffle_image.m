function y = shuffle_image(d,m,n)
q = size(d);
c = [];
for  i = 1:q(1)/m:q(1)
   for j = 1:q(2)/m:q(2)
 k = d(i:i+q(1)/m-1,j:j+q(2)/n-1,1:3);
 c = cat(3,c,k);
   end
end

new_image=[];
   for i = 1:1:m
       b=[];
       for j= 1:3:3*n
           b=cat(1,b,c(:,:,[(i-1)*30+j:1:(i-1)*30+j+2]));
       end
       new_image = cat(2,new_image,b);
   end
   y = new_image;