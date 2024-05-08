# Bioinformatics_Skills

This is a repo that contains all scripts used for our Bioinformatics group project about Dynamic Models. 

### Project Description:  
This project is about using dynamic models to learn about population dynamics regarding 3-species systems. In this case, we will be looking at a system containing plants, hares and lynxes. We are required to perform two main tasks. For *Task 1* we are required to describe the model and it's parameters. For *Task 2* we are required to look into three different scenarios and find parameter solutions for each scenario. For this second task we have been given some recommended initial starting values for the model parameters, and we will adjust them until we find the correct solutions.  We are also required to include time-series plots, state-space plots and final model parameters. This project will be done in Matlab and is due on the 14th of May. 


#### Course Information:
- **Course Name:** Bioinformatics Skills
- **Course Code:** SKI2102

#### Group Members:
- Nieka-Lee Ireland (i6323898)  
- Sabrina Scuitto (add here)  
- Tom van Wersch (add here)  


#### Task 1
###### Describing the model and its parameters 

- y refers to the population size of the 3 species. 
- y1 for plant's population
- y2 for hare's population
- y3 for lynx's population.
- d1 and d2 define the half saturation density. The half saturation density is the concentration of a limiting nutrient at which the population's growth rate is half of its maximum potential rate. In this specific case, we have plant mass, number of herbivores (hare) and number of carnivores (lynx).

###### Observations:  
In absence of hares, the plant mass would increase exponentially (but it is unrealistic, because of some constraints in nature, so the plant mass growth logistically. 

At higher plant mass density, the hare's consumption rate increases (reaches max saturation).

The average number of births per individual (per capita birth rate) is proportional to the number of food consumed (plant mass for hares and hares for lynx). In other words, the number of hares's birth depends on the availability of plant mass, higher plant mass, higher chances of hares reproduction. Regarding lynx, higher availability of hares, higher chances of survival for lynx and their following reproduction.

The average number of deaths per individual (per capita death rate) is a constant.
- d1 = death rate of hare
- d2 = death rate of lynx lynx

The rate at which carnivore (lynx) consumes the herbivore (hare) depends on the saturation of hares (they reach the maximum value).

Predator success rate is denoted by "a". So the rate at which the lynx eats the hares. How efficiently the predator succeeds in catching the prey.
- a1 = plant (consumption of plants by the hares
- a2 = cosumption of hares by the plants 

The predator population growth due to catching a prey is represented by "b". So the rate at which the population of lynx rises because of the consumption of hares. It is about how the predation has an impact of predator's population dynamics.
- b1 = saturation point for plant consumption  
- b2 = saturation point for hare consumption 


- w is the max consumption rate
