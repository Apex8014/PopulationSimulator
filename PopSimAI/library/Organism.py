import random

class Organism():
    #initialization
    def __init__(self, name, population, birthRate, carryingCapacity, eatingRate = 0, prey = ["none"], AI = False):
        self.name = name
        self.population = population
        self.birthRate = birthRate
        self.carryingCapacity = carryingCapacity
        self.eatingRate = eatingRate
        self.prey = prey
        self.originalValues = [birthRate, carryingCapacity]
        self.AI = AI
    """
    if it is a plant, grow the popuation, otherwise, if the are not a plant, 
        if there are enough prey, grow the population, eat the prey, 
        if there is not enough prey, half the population.
    """ 
    def growPopulation(self):
        #detects if its a plant
        for i in range(len(self.prey)):
            if self.prey[i] != "none":
                #detects if there is enough prey
                if self.prey[i].population > (int)(self.eatingRate*self.population/len(self.prey)):
                    #eats prey
                    self.prey[i].removePopulation((int)(self.eatingRate*self.population/len(self.prey)))
                    #grows population
                    self.population += (int)((self.population*self.birthRate*(self.carryingCapacity-self.population)/self.carryingCapacity))
                else:
                    #Halves the population
                    self.population /= 2
                    self.population = (int)(self.population)
            else:
                #grows population if its a plant
                self.population += (int)((self.population*self.birthRate*(self.carryingCapacity-self.population)/self.carryingCapacity))
        #random flucuation (migration, deaths by other causes, higher than expected birth rates)
        """
        try:
            self.population += random.randint((int)(self.carryingCapacity*(1-(self.carryingCapacity-self.population)/self.carryingCapacity)*-0.1),(int)(self.carryingCapacity*(1-(self.carryingCapacity-self.population)/self.carryingCapacity)*0.1))
        except:
            pass
        if self.population < 0:
            self.population = 0
        """
        #Determines if an event happens
        self.birthRate, self.carryingCapacity = self.originalValues
        if len(self.prey) == 1:
            try:
                if self.prey[0].prey[0] == "none":
                    #Events for herbivores
                    self.randEventVal = random.randint(1,25)
                    if self.randEventVal > 24:
                        if not self.AI:
                            print("The plants were not very nutritous this year so some herbivores didnt get all the nutrients they needed.")
                        self.population += random.randint(-50,0)
                    elif self.randEventVal > 23:
                        if not self.AI:
                            print("The plants were very nutritous! the herbivores gain a 10%% increase in birth rate and 10%% decrease in eating rate.")
                        self.eatingRate *= 1.10
                        self.birthRate *= 1.10
            except:
                #Events for plants
                self.randEventVal = random.randint(1,25)
                if self.randEventVal > 24:
                    if not self.AI:
                        print("There was a fire that burned the forest! 50%% of the plants died.")
                    self.population /= 2
                    self.population = (int)(self.population)
                elif self.randEventVal > 23:
                    if not self.AI:
                        print("Extra nutrients were introduced into the soil and increased the plant growth rate, carrying capacity, and population by 25%%")
                    self.population *= 1.25
                    self.population = (int)(self.population)
                    self.birthRate *= 1.25
                    self.carryingCapacity *= 1.25
        else:
            if self.prey[1].prey[0] == "none":
                #Events for omnivores
                self.randEventVal = random.randint(1,25)
                if self.randEventVal > 24:
                    if not self.AI:
                        print("The plants were not very nutritous this year so some omnivores didnt get all the nutrients they needed.")
                    self.population += random.randint(-50,0)
                elif self.randEventVal > 23:
                    if not self.AI:
                        print("The plants were very nutritous! the omnivores gain a 10%% increase in birth rate and 10%% decrease in eating rate.")
                    self.eatingRate *= 1.10
                    self.birthRate *= 1.10
                if self.randEventVal > 22:
                    if not self.AI:
                        print("The herbivores had a deadly virus that wiped out 50%% of the predator population")
                    self.population /= 2
                    self.population = (int)(self.population)
                elif self.randEventVal > 21:
                    if not self.AI:
                        print("The predators ate other invasive species instead of their typical prey so their population increased")
                    self.prey[0].growPopulation()
            else:
                #Events for predators
                self.randEventVal = random.randint(1,25)
                if self.randEventVal > 24:
                    if not self.AI:
                        print("The herbivores had a deadly virus that wiped out 50%% of the predator population")
                    self.population /= 2
                    self.population = (int)(self.population)
                elif self.randEventVal > 23:
                    if not self.AI:
                        print("The predators ate other invasive species instead of their typical prey so their population increased")
                    self.prey[0].growPopulation()
        if self.population < 0:
            self.population = 0
    """
    Removes an amount from a population
    Params:
        amount: the amount removed from a population
    """
    def removePopulation(self, amount):
        self.population -= amount
        if self.population < 0:
            self.population = 0