#import organism class
from library.GenerationalAI import AI
from library.Organism import Organism
import math
import random

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
        randomAIList.append(AI([random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000)],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000]))
    for i in range(184):
        generatedAIList.append(AI([random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000)],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000]))

#main
generateInitialAI()
#repeats until you chose to end the simulation
for iterations in range(2000):
    for i in range(184):
        #initializes per randomAI
        generations = 1
        plant = Organism("Berries",randomAIList[i].allData[0],randomAIList[i].allData[1],randomAIList[i].allData[2],AI = True)
        herbivore = Organism("Artic Hares",randomAIList[i].allData[3],randomAIList[i].allData[4],randomAIList[i].allData[5],randomAIList[i].allData[6],prey = [plant],AI = True)
        omnivore = Organism("Arctic Foxes",randomAIList[i].allData[7],randomAIList[i].allData[8],randomAIList[i].allData[9],randomAIList[i].allData[10],prey = [plant,herbivore],AI = True)
        predator = Organism("Perigine Falcon",randomAIList[i].allData[11],randomAIList[i].allData[12],randomAIList[i].allData[13],randomAIList[i].allData[14],prey = [herbivore,omnivore],AI = True)
        currentScore = 0
        while True:
            #grows the population
            plant.growPopulation()
            herbivore.growPopulation()
            omnivore.growPopulation()
            predator.growPopulation()
            #Adds to score
            currentScore +=  generations * generations * ((plant.population/plant.carryingCapacity) * 0.1 + (herbivore.population/herbivore.carryingCapacity) + (omnivore.population/omnivore.carryingCapacity) * 10 + (predator.population/predator.carryingCapacity) * 100)
            #Prints if a species dies
            randomAIList[i].generations = generations
            if plant.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            if herbivore.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            if omnivore.population <= 0:
                #currentScore = generations
                currentScore *= 0.50
                randomAIList[i].score += currentScore
                break
            if predator.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                randomAIList[i].score += currentScore
                break
            generations += 1
    for i in range(184):
        #initializes per generated
        generations = 1
        plant = Organism("Berries",generatedAIList[i].allData[0],generatedAIList[i].allData[1],generatedAIList[i].allData[2],AI = True)
        herbivore = Organism("Artic Hares",generatedAIList[i].allData[3],generatedAIList[i].allData[4],generatedAIList[i].allData[5],generatedAIList[i].allData[6],prey = [plant],AI = True)
        omnivore = Organism("Arctic Foxes",generatedAIList[i].allData[7],generatedAIList[i].allData[8],generatedAIList[i].allData[9],generatedAIList[i].allData[10],prey = [plant,herbivore],AI = True)
        predator = Organism("Perigine Falcon",generatedAIList[i].allData[11],generatedAIList[i].allData[12],generatedAIList[i].allData[13],generatedAIList[i].allData[14],prey = [herbivore,omnivore],AI = True)
        currentScore = 0
        while True:
            #grows the population
            plant.growPopulation()
            herbivore.growPopulation()
            omnivore.growPopulation()
            predator.growPopulation()
            #Adds to score
            currentScore += generations * generations * ((plant.population/plant.carryingCapacity)*0.1 + (herbivore.population/herbivore.carryingCapacity) + (omnivore.population/omnivore.carryingCapacity)*10 + (predator.population/predator.carryingCapacity)*100)
            #Prints if a species dies
            generatedAIList[i].generations = generations
            if plant.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            if herbivore.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            if omnivore.population <= 0:
                #currentScore = generations
                currentScore *= 0.50
                generatedAIList[i].score += currentScore
                break
            if predator.population <= 0:
                #currentScore = generations
                currentScore *= 0.75
                generatedAIList[i].score += currentScore
                break
            generations += 1
    # Finds best two generated and best two random AI
    randomAI = [randomAIList[0],randomAIList[1]]
    for i in range(182):
        if randomAIList[i+2].score > randomAI[0].score:
            randomAI[0] = randomAIList[i+2]
        elif randomAIList[i+2].score > randomAI[1].score:
            randomAI[1] = randomAIList[i+2]
    generatedAI = [generatedAIList[0],generatedAIList[1]]
    for i in range(182):
        if generatedAIList[i+2].score > generatedAI[0].score:
            generatedAI[0] = generatedAIList[i+2]
        elif generatedAIList[i+2].score > generatedAI[1].score:
            generatedAI[1] = generatedAIList[i+2]
    print("Generated AI 1 \nScore:" + str(generatedAI[0].score) + "\nSettings: " + str(generatedAI[0].allData))
    print(str(generatedAI[0].generations))
    print("Generated AI 2 \nScore:" + str(generatedAI[1].score) + "\nSettings: " + str(generatedAI[1].allData))
    print(str(generatedAI[1].generations))
    print("Random AI 1 \nScore:" + str(randomAI[0].score) + "\nSettings: " + str(randomAI[0].allData))
    print(str(randomAI[0].generations))
    print("Random AI 2 \nScore:" + str(randomAI[1].score) + "\nSettings: " + str(randomAI[1].allData))
    print(str(randomAI[1].generations))
    #regenerates AI
    allAI = randomAI + generatedAI
    randomAIList = []
    generatedAIList = [i for i in allAI]
    #generates new AI
    for x in range(4):
        for y in range(4):
            if not x==y:
                generatedAIList = allAI[x].regenerate(allAI[y], generatedAIList)
    #adds winning AI to list
    #remakes random AI
    for i in range(184):
        generatedAIList[i].score = 0
        generatedAIList[i].generations = 0
    print((iterations+1)/2000)
    for i in range(184):
        randomAIList.append(AI([random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000)],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000],[random.randint(1,1000000000), random.randint(1,20000)/10000, random.randint(1,1000000000),random.randint(1,20000)/10000]))