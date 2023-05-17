clc;
clear all;
close all;
y=csvread("2020_ten_bent_coins.csv");

theta=rand(1,10);
h = sum(y,2); %returns column vector with sum of rows of y
t = 100-h;

th(1,:) = theta;

for a=1:100
p = zeros(500,10);
for i=1:500
    for j=1:10
        p(i,j)=(th(a,j).^h(i,1)).*((1-th(a,j)).^t(i,1));
    end
end
np = p;
s= sum(p,2);
for i=1:500
    for j=1:10
        np(i,j)=p(i,j)/s(i,1);
    end
end

heads = zeros(500,10);

for i=1:500
    for j=1:10
        heads(i,j)=np(i,j)*h(i,1);
    end
end
tails = zeros(500,10);
for i=1:500
    for j=1:10
        tails(i,j)=np(i,j)*t(i,1);
    end
end
sumheads=sum(heads,1);
sumtails=sum(tails,1);
for i=1:10
    th(a+1,i) = sumheads(1,i)/(sumheads(1,i)+sumtails(1,i)); 
end
end
th
