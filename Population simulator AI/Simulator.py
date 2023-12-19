"""
Name: Ash Prince
Date: 11/2/2023
Class: Mr. Guilaume, 2023, Tri 1
Description: A simulation run in python using constructors to simulate an ecosystem. Random events can affect the growth of species and in the end all the data collected is graphed.
"""

#import organism class
from library.Organism import Organism
import matplotlib.pyplot as pyplot

#Asks a question and gets "y" or "n" then returns a boolean based on input
def askForYN(question):
    result = input(question + "(y/n): ")
    while result not in ["y","n"]:
        result = input("Invalid response, please select \"y\" or \"n\": ")
    result = result == "y"
    return result

def drawGraph():
    pyplot.legend()
    pyplot.xlabel("Generation")
    pyplot.ylabel("Population")
    if askForYN("Do you want a logistical graph?"):
        pyplot.yscale("log")
    pyplot.plot(generationsList, generationalData["plant"], label = plant.name)
    pyplot.plot(generationsList, generationalData["herbivore"], label = herbivore.name)
    pyplot.plot(generationsList, generationalData["omnivore"], label = omnivore.name)
    pyplot.plot(generationsList, generationalData["predator"], label = predator.name)
    pyplot.show()

def finalResults():
    print("Final results:")
    print("The ecosystem survived " + (str)(generations) + " generation(s)")
    print("There were " + (str)(plant.population) + " plants")
    print("There were " + (str)(herbivore.population) + " herbivores")
    print("There were " + (str)(omnivore.population) + " omnivores")
    print("There were " + (str)(predator.population) + " predators")

#initialization
if askForYN("Do you want to use a preset simulation?"):
    preset = input("Choose a preset(1 (First test), 2 (Base), 3 (Previous highscore: 1150 generations), 4 (Previous highscre: 1380 generations), 5 (previously most consistent), 6 (previous most consistent and previous highscore: 1669 generations), 7 (current most consistent & current highscore: 2400 generations)): ")
    while preset not in ["1","2","3","4","5","6","7"]:
        preset = input("Please enter 1, 2, 3, 4, 5, 6, or 7: ")
    if preset == "1":
        plant = Organism("Berries", 200, 1.0, 1000)
        herbivore = Organism("Arctic hares", 200, 0.9, 800, 0.25, [plant])
        omnivore = Organism("Arctic Foxes", 200, 0.75, 400, 0.5, [herbivore,plant])
        predator = Organism("Perigine Falcons", 200, 0.5, 200, 1, [herbivore,omnivore])
    elif preset == "2":
        plant = Organism("Berries", 10000, 2.0, 100000)
        herbivore = Organism("Arctic hares", 1000, 2.0, 10000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 1.5, 1000, 2.5, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 100, 0.75, [herbivore,omnivore])
    elif preset == "3":
        plant = Organism("Berries", 10000, 2.0, 100000)
        herbivore = Organism("Arctic hares", 1000, 2.0, 10000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 1.8, 1000, 2.5, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 100, 0.7, [herbivore,omnivore])
    elif preset == "4":
        plant = Organism("Berries", 10000, 2.0, 100000)
        herbivore = Organism("Arctic hares", 1000, 2.2, 10000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 2.1, 1000, 2.4, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 100, 0.7, [herbivore,omnivore])
    elif preset == "5":
        plant = Organism("Berries", 10000, 2.0, 100000)
        herbivore = Organism("Arctic hares", 1000, 2.4, 10000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 2.3, 1000, 2.4, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 100, 0.7, [herbivore,omnivore])
    elif preset == "6":
        plant = Organism("Berries", 10000, 2.0, 1000000)
        herbivore = Organism("Arctic hares", 1000, 2.4, 100000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 2.3, 10000, 2.4, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 1000, 0.7, [herbivore,omnivore])
    else:
        plant = Organism("Berries", 10000, 2.0, 10000000)
        herbivore = Organism("Arctic hares", 1000, 2.4, 1000000, 1.25, [plant])
        omnivore = Organism("Arctic Foxes", 100, 2.3, 100000, 2.4, [herbivore,plant])
        predator = Organism("Perigine Falcons", 10, 0.75, 10000, 0.7, [herbivore,omnivore])
else:
    print("Tip: The lower percentage of the starting population is of the max population, the more stable the ecosystem is. Also, omnivores are the most important to the habitat but are also the hardest to keep alive.")
    predator = ""
    while predator == "":
        try:
            plant = Organism(input("Enter name of plant: "), (int)(input("Enter intial population of plant: ")), (float)(input("Enter birth rate of plant: ")), (int)(input("Input carrying capacity for plant: ")))
            herbivore = Organism(input("Enter name of herbivore: "), (int)(input("Enter intial population of herbivore: ")), (float)(input("Enter birth rate of herbivore: ")), (int)(input("Input carrying capacity for herbivore: ")), (float)(input("Input eating rate of herbivore: ")), [plant])
            omnivore = Organism(input("Enter name of omnivore: "), (int)(input("Enter intial population of omnivore: ")), (float)(input("Enter birth rate of omnivore: ")), (int)(input("Input carrying capacity for omnivore: ")), (float)(input("Input eating rate of omnivore: ")), [herbivore,plant])
            predator = Organism(input("Enter name of predator: "), (int)(input("Enter intial population of predator: ")), (float)(input("Enter birth rate of predator: ")), (int)(input("Input carrying capacity for predator: ")), (float)(input("Input eating rate of predator: ")), [herbivore,omnivore])
        except:
            print("Be careful and make si=ure you are entering the proper input values for each question.")
            plant = Organism(input("Enter name of plant: "), (int)(input("Enter intial population of plant: ")), (float)(input("Enter birth rate of plant: ")), (int)(input("Input carrying capacity for plant: ")))
            herbivore = Organism(input("Enter name of herbivore: "), (int)(input("Enter intial population of herbivore: ")), (float)(input("Enter birth rate of herbivore: ")), (int)(input("Input carrying capacity for herbivore: ")), (float)(input("Input eating rate of herbivore: ")), [plant])
            omnivore = Organism(input("Enter name of omnivore: "), (int)(input("Enter intial population of omnivore: ")), (float)(input("Enter birth rate of omnivore: ")), (int)(input("Input carrying capacity for omnivore: ")), (float)(input("Input eating rate of omnivore: ")), [herbivore,plant])
            predator = Organism(input("Enter name of predator: "), (int)(input("Enter intial population of predator: ")), (float)(input("Enter birth rate of predator: ")), (int)(input("Input carrying capacity for predator: ")), (float)(input("Input eating rate of predator: ")), [herbivore,omnivore])
endSim = False
generations = 0
generationalData = {"plant":[],"herbivore":[],"omnivore":[],"predator":[]}

runTillOver = askForYN("(Highly Suggested)Do you want to continue until the population ends?")

#main
#repeats until you chose to end the simulation
while not endSim or runTillOver:
    #grows the population
    plant.growPopulation()
    herbivore.growPopulation()
    omnivore.growPopulation()
    predator.growPopulation()
    #Adds data for graph use
    generationalData["plant"].append(plant.population)
    generationalData["herbivore"].append(herbivore.population)
    generationalData["predator"].append(predator.population)
    generationalData["omnivore"].append(omnivore.population)
    #Prints if a species dies
    if plant.population <= 0:
        print("All the plants died, the whole ecosystem is destroyed.")
        break
    if herbivore.population <= 0:
        print("All the herbivores died, only plants remain.")
        break
    if omnivore.population <= 0:
        print("All the omnivores died, only plants and herbivores remain.")
        break
    if predator.population <= 0:
        print("All the predators died, the herbivores grow out of control ,eat all the plants, and the whole ecosystem is destroyed.")
        break
    generations += 1
    #prints population values
    print(plant.name + " population: " + (str)(plant.population))
    print(herbivore.name + " population: " + (str)(herbivore.population))
    print(omnivore.name + " population: " + (str)(omnivore.population))
    print(predator.name + " population: " + (str)(predator.population))
    #determines to end the game or not
    if not  runTillOver:
        endSim = not askForYN("Do you want to continue the simulation?")
#prints end results
finalResults()
generationsList = [i for i in range(generations + 1)]
#makes graph
drawGraph()