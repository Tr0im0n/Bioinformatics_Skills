# Bioinformatics_Skills

This is a repo that contains all scripts used for our Bioinformatics group project about Dynamic Models. 

### Project Description:  
This project is about using dynamic models to learn about population dynamics regarding 3-species systems. In this case, we will be looking at a system containing plants, hares and lynxes. We are required to perform two main tasks. For *Task 1* we are required to describe the model and it's parameters. For *Task 2* we are required to look into three different scenarios and find parameter solutions for each scenario. For this second task we have been given some recommended initial starting values for the model parameters, and we will adjust them until we find the correct solutions.  We are also required to include time-series plots, state-space plots and final model parameters. This project will be done in Matlab and is due on the 14th of May. 


###### Course Information:
- **Course Name:** Bioinformatics Skills
- **Course Code:** SKI2102

###### Group Members:
- Nieka-Lee Ireland (i6323898)  
- Sabrina Scuitto (i6300699)  
- Tom van Wersch (add here)  


### Task 1
##### *Describing the model and its parameters*

- The array denoted by **"y"** holds the values for the initial population size of each of the three species: **"y1"** showing the initial plant population; **"y2"** showing the initial hare population; and **"y3"** showing the initial lynx population.
- The average number of deaths is described as a constant for each species (per capita death rate). The death rate of the hares is described by **"d1"** and the death rate of the lynxes is described by **"d2"**. In this scenario, the plants do not die unless they are eaten, therefore the plants do not have a death rate.
- The predator success rate is denoted by **"a"** and describes how successful a predator will be if it comes into contact with its prey (in other words: how likely a prey is to die if it comes in contact with a predator). The predation rate of the hares towards the plants is described by **"a1"** (consumption of plants by hares) and the predation rate of the lynxes towards the hares is described by **"a2"** (consumption of hares by lynxes).
- The saturation point is denoted by **"b"** and describes the maximum number of prey a predator can eat before it gets full. The saturation point for plant consumption by hares is described by **"b1"** and the saturation point for hare consumption by lynxes is described by **"b2"**. 



##### *Observations:*
In the initial plot, it can be observed that if there were no hares, the plant mass would increase exponentially. However, this is not realistic because there are certain limitations in nature, which means the plant mass grows logistically. 

The average number of births per species is directly proportional to the amount of food consumed. In other words, when there is a high plant mass, there are higher chances of hare reproduction. Similarly, for lynx, the availability of hares is directly linked to their survival and reproduction rate.
The rate at which a carnivore (lynx) consumes a herbivore (hare) depends on the saturation of hares. This means that when hares reach their maximum value, the consumption rate of lynx also reaches its maximum value because of their large availability.

