function dydt = plants_hare_lynx(t,y,a1,a2,b1,b2,d1,d2)

% change here

dydt = zeros(3,1);

dydt(1) = y(1)*(1-y(1)) - ((a1*y(1))/(1+b1*y(1)))*y(2);
%the per herbivore consumption of plants saturates (reaches max value) with 
% increasing plant density.  &changesssss
dydt(2) = ((a1*y(1))/(1+b1*y(1)))*y(2)-d1*y(2)-(a2*y(2)/(1+b2*y(2)))*y(3);
dydt(3) = (a2*y(2)/(1+b2*y(2)))*y(3) - d2*y(3);
%The rate at which the predator consumes the herbivore is a saturating 
% function of herbivore density.

%based on the equation r and K are assumed to be 1 to simplify the
%equations.
end
%% y refers to the population size of the 3 species. 
%y1 for plant's population
%y2 for hare's population
%y3 for lynx's population.
%% d1 and d2 define the half saturation density.
% The half saturation density is the concentration of a limiting nutrient 
% at which the population's growth rate is half of its maximum potential rate.
%In this specific case, we have plant mass, number of herbivores (hare) and number
%of carnivores (lynx).

%% Observations. 
   %In absence of hares, the plant mass would increse exponentially (but it is
%unrealistic, because of some constraints in nature, so the plant mass
%growth logistically. 

  % At higher plant mass density, the hare's consumption rate increases
% (reaches max saturation).

  % The average number of births per individual (per capita birth rate) is
% proportional to the number of food consumed (plant mass for hares and
% hares for lynx). In other words, the number of hares's birth depends on
% the availability of plant mass, higher plant mass, higher chances of
% hares reproduction. Regarding lynx, higher availability of hares, higher
% chances of survival for lynx and their following reproduction.

 % The average number of deaths per individual (per capita death rate) is a 
 % constant.
% d1=lynx
% d2=hare

 % the rate at which carnivore (lynx) consumes the herbivore (hare) depends
% on the saturation of hares (they reach the maximum value).

 % the a= predator success rate. So the rate at which the lynx eats the
% hares. How efficiently the predator succeeds in catching the prey.
% a1=lynx
% a2=hare

 %the b=the predator population growth due to catching a prey. So the rate
%at which the population of lynx rises becasue of the consumption of
%hares. It is about how the predation has an impact of predator's
%population dynamics.
 %b1=lynx
 %b2=hare


%% w is the max consumption rate