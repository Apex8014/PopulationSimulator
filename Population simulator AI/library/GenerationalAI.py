class AI():
    def __init__(self, plantData = [], herbivoreData = [], omnivoreData = [], predatorData = [], allData = []):
        self.plantData = plantData
        self.herbivoreData = herbivoreData
        self.omnivoreData = omnivoreData
        self.predatorData = predatorData
        if allData == []:
            self.allData = self.plantData + self.herbivoreData + self.omnivoreData + self.predatorData
        else:
            self.allData = allData
        self.score = 0
    
    def regenerate(self, remainingAI, AIList):
        #Starts with 184 AIs, kills 180, then makes 180 more via conbination, then makes 184 random ones
        self.indexChange = -1
        for i in range(self.allData.length()):
            self.indexChange += 1
            #Changes one value of all data list
            AIList[AIList.length()] = AI(allData = (self.allData[0:i] + remainingAI.allData[i] + self.allData[i+1:]))
            return AIList
        
    def delete(self, AIList):
        #Deletes this AI
        AIList.remove(self)
        self = ""
        return AIList
