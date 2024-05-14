function [dydt] = plants_hare_lynx_(t,y,a1,a2,b1,b2,d1,d2)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
dydt = zeros(3,1);

dydt(1) = y(1)*(1-y(1)) - ((a1*y(1))/(1+b1*y(1)))*y(2); 
dydt(2) = ((a1*y(1))/(1+b1*y(1)))*y(2)-d1*y(2)-(a2*y(2)/(1+b2*y(2)))*y(3);
dydt(3) = (a2*y(2)/(1+b2*y(2)))*y(3) - d2*y(3);

end 