function y = ramka(arr,lig,col)
q = size(arr);
for i = 1 : 3;
arr(1:lig,1:q(2),i) = col(i)*255;
arr(1:q(1),1:lig,i) = col(i)*255;
arr(q(1)-lig:q(1),1:q(2),i) = col(i)*255;
arr(1:q(1),q(2)-lig:q(2),i) = col(i)*255;
end
y=arr;
