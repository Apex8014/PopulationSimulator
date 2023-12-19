#import organism class
from library.GenerationalAI import AI
from library.Organism import Organism
import matplotlib.pyplot as pyplot
import math

#Asks a question and gets "y" or "n" then returns a boolean based on input
def askForYN(question):
    result = input(question + "(y/n): ")
    while result not in ["y","n"]:
        result = input("Invalid response, please select \"y\" or \"n\": ")
    result = result == "y"
    return result

def finalResults():
    print("Final results:")
    print("The ecosystem survived " + (str)(generations) + " generation(s)")
    print("There were " + (str)(plant.population) + " plants")
    print("There were " + (str)(herbivore.population) + " herbivores")
    print("There were " + (str)(omnivore.population) + " omnivores")
    print("There were " + (str)(predator.population) + " predators")

#AI initialization
randomAIList = []
generatedAIList = []
def generateInitialAI():
    for i in range(184):
        randomAIList[i] = AI([math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000)],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000])
    for i in range(184):
        generatedAIList[i] = AI([math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000)],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000],[math.randint(1,1000000000), math.randint(0,20000)/10000, math.randint(1,1000000000),math.randint(0,20000)/10000])

#main
#repeats until you chose to end the simulation
for i in range(250):
    for i in range(184):
        #initializes per randomAI
        generations = 1
        plant = Organism("Berries",randomAIList[i].allData[0],randomAIList[i].allData[1],randomAIList[i].allData[2])
        herbivore = Organism("Artic Hares",randomAIList[i].allData[3],randomAIList[i].allData[4],randomAIList[i].allData[5],randomAIList[i].allData[6])
        omnivore = Organism("Arctic Foxes",randomAIList[i].allData[7],randomAIList[i].allData[8],randomAIList[i].allData[9],randomAIList[i].allData[10])
        predator = Organism("Perigine Falcon",randomAIList[i].allData[11],randomAIList[i].allData[12],randomAIList[i].allData[13],randomAIList[i].allData[14])
        currentScore = 0
        while True:
            #grows the population
            plant.growPopulation()
            herbivore.growPopulation()
            omnivore.growPopulation()
            predator.growPopulation()
            #Adds to score
            currentScore += ((plant.population/plant.carryingCapacity) + (herbivore.population/herbivore.carryingCapacity) + (omnivore.population/omnivore.carryingCapacity) + (predator.population/predator.carryingCapacity)) * generations 
            #Prints if a species dies
            if plant.population <= 0:
                print("All the plants died, the whole ecosystem is destroyed.")
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            if herbivore.population <= 0:
                print("All the herbivores died, only plants remain.")
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            if omnivore.population <= 0:
                print("All the omnivores died, only plants and herbivores remain.")
                currentScore *= 0.50
                randomAIList[i].score += currentScore
                break
            if predator.population <= 0:
                print("All the predators died, the herbivores grow out of control ,eat all the plants, and the whole ecosystem is destroyed.")
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            generations += 1
    for i in range(184):
        #initializes per generated
        generations = 1
        plant = Organism("Berries",generatedAIList[i].allData[0],generatedAIList[i].allData[1],generatedAIList[i].allData[2])
        herbivore = Organism("Artic Hares",generatedAIList[i].allData[3],generatedAIList[i].allData[4],generatedAIList[i].allData[5],generatedAIList[i].allData[6])
        omnivore = Organism("Arctic Foxes",generatedAIList[i].allData[7],generatedAIList[i].allData[8],generatedAIList[i].allData[9],generatedAIList[i].allData[10])
        predator = Organism("Perigine Falcon",generatedAIList[i].allData[11],generatedAIList[i].allData[12],generatedAIList[i].allData[13],generatedAIList[i].allData[14])
        currentScore = 0
        while True:
            #grows the population
            plant.growPopulation()
            herbivore.growPopulation()
            omnivore.growPopulation()
            predator.growPopulation()
            #Adds to score
            currentScore += ((plant.population/plant.carryingCapacity) + (herbivore.population/herbivore.carryingCapacity) + (omnivore.population/omnivore.carryingCapacity) + (predator.population/predator.carryingCapacity)) * generations 
            #Prints if a species dies
            if plant.population <= 0:
                print("All the plants died, the whole ecosystem is destroyed.")
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            if herbivore.population <= 0:
                print("All the herbivores died, only plants remain.")
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            if omnivore.population <= 0:
                print("All the omnivores died, only plants and herbivores remain.")
                currentScore *= 0.50
                generatedAIList[i].score += currentScore
                break
            if predator.population <= 0:
                print("All the predators died, the herbivores grow out of control ,eat all the plants, and the whole ecosystem is destroyed.")
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            generations += 1
    randomAI = [randomAIList[0],randomAIList[1]]
    for i in range(182):
        if randomAIList[i+2].score > randomAI[0].score:
            randomAI[0] = randomAIList[i+2]
        elif randomAIList[i+2].score > randomAI[1].score:
            randomAI[1] = randomAIList[i+2]
    randomAI = [randomAIList[0],randomAIList[1]]
    for i in range(182):
        if randomAIList[i+2].score > randomAI[0].score:
            randomAI[0] = randomAIList[i+2]
        elif randomAIList[i+2].score > randomAI[1].score:
            randomAI[1] = randomAIList[i+2]