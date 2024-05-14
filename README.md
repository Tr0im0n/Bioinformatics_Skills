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
- Tom van Wersch (i6293010)  


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


### Task 2
##### Scenario 1
*The system exhibits stable oscillations with a periodicity of approximately 70 months.*


This model presents a period oscillation of about 40-50 months, so it is not stable. As the population of hares increases, the lynxes have more food to survive and reproduce. When reaching the highest saturation point, the lynxes put more pressure on hare reproduction, leading to their decrease. Their decrease results in a following increase in plant mass growth. 

##### Scenario 2
*The lynx population goes extinct (population very close to zero) after a year, plants and hares stabilize within 120 months.*


Based on the resulting plot, we can see that the population of lynxes becomes extinc (reaches zero) around the 60 month mark. The hares and the plants begin to stabalise their population around the 120 month mark. This was done by figuring out how to make the lynxes go extinct, without simply killing all the hares (we had to make sure that some hares were still alive in order to stabalise the hare-plant relationship). After inspecting various variables and making educated judgements about which variables to change and when, the requested  scenerio was obtained. 


##### Scenario 3
*The system shows chaotic behavior and the lynx population peaks twice within the 200-months period. What makes this behavior chaotic and not oscillating or random? Hint: Chaotic behavior is deterministic, sensitive to initial conditions, bounded and irregular.*


As you can see in the first graph, the lynx population peaks twice. \
The changes made in this simulation were a slight increase in d2 and an increase in the starting lynx population. The reason that we chose to increase d2, is that the lynx population is very stable because that death rate was so low. Even when the hare population falls the lynx population will only change a small amount. So to increase instability we increased the lynx death rate. Then we messed around with the starting lynx population and found that the model was sensitive toward that input. If you were to increase or decrease it you get quite a different result for example:\
9: Here the system has a lot fewer oscillations. \
11: The population first falls for quite a long time than it oscillates upwards. \
This brings us to whether the system is chaotic. The 4 criteria mentioned for a chaotic system are: deterministic, sensitive to initial conditions, bounded and irregular. \
The system is deterministic, because, well, we have made the model ourselves and you can see the equations right here. (in the plants_hare_lynx_.m file)\
The system is also bounded. The grass has a carrying capacity of 1, so the grass population won't increase beyond there, the hares grow by eating grass, so are bound by the amount of grass present, same for the lynx they grow by eating hares, so are bound by their population size. The population also have a lower bound of 0, as you can't have a negative population size. \
I am unsure to call the system irregular, the state space seems quite clean. \


Personal note: I'm still a bit unsure how chaotic a system needs to be to qualify as chaotic. I'm not convinced about making this system chaotic. But  it would be interesting to see it. If you are looking at the state space, with this type of model you are bound to find a stable path through it. I guess you could ask how long a loop needs to be for it to qualify as chaotic. \
Second note: For ease of use and out of my own personal interest I made the script population_slider_simulation.py . It is a standalone script to simulate and show these population changes and gives you sliders to change the variables and initial conditions. This made it a lot easier to test different values. 





