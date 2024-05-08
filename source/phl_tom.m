function [dydt] = phl_tom(t,y,m1,m2,h1,h2,d1,d2)
dydt = zeros(3,1);

% r1 = 1;
% m1 = 1;
% h1 = 70;
% m2 = 1;
% h2 = 70

% dydt(1) = y(1)*(1-y(1)) - m1*y(1)*y(2)/(h1+y(1)); 
% dydt(2) = m1*y(1)*y(2)/(h1+y(1)) - m2*y(2)*y(3)/(h2+y(2)) - d1*y(2);
% dydt(3) = m2*y(2)*y(3)/(h2+y(2)) - d2*y(3);

dydt(1) = y(1) * (1 - y(1)) - (m1 * y(1) * y(2)) / (h1 + y(1));
dydt(2) = (m1 * y(1) * y(2)) / (h1 + y(1)) - (m2 * y(2) * y(3)) / (h2 + y(2)) - d1 * y(2);
dydt(3) = (m2 * y(2) * y(3)) / (h2 + y(2)) - d2 * y(3);

% Equations
% dydt = zeros(3,1);
% dydt(1) = y(1) * (1 - y(1)) - (m1 * y(1) * y(2)) / (h1 + y(1));
% dydt(2) = (m1 * y(1) * y(2)) / (h1 + y(1)) - (m2 * y(2) * y(3)) / (h2 + y(2)) - d1 * y(2);
% dydt(3) = (m2 * y(2) * y(3)) / (h2 + y(2)) - d2 * y(3);

end 