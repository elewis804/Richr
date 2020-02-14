import random


class getRandomChar():
    def __init__(self):
        self.whatChar()

    def whatChar(self):
        charType = random.randrange(1, 11)
        if charType == 1:
            self.getPredChar()
        else:
            self.getRndChar()

    def getPredChar(self):
        lineList = []
        lines = open("Characters.txt", "r")
        for line in lines:
            lineList.append(line)
        l = random.randrange(0, len(lineList))
        lineChoice = lineList[l]
        cAttr = lineChoice.split("/")
        self.cName = cAttr[0]
        self.cDesc = cAttr[1]
        self.cGrant = cAttr[2]
        self.cDeny = cAttr[3]

    def getRndChar(self):
        dLineList = []
        nameList = []
        names = open("Names.txt", "r")
        for line in names:
            nameList.append(line)
        nameChoice = random.randrange(0, len(nameList))
        self.cName = nameList[nameChoice]
        descriptions = open("Description.txt", "r")
        for dLine in descriptions:
            dLineList.append(dLine)
        descriptionChoice = random.randrange(0, len(dLineList))
        descLine = list(dLineList[descriptionChoice].split("/"))
        self.cDesc = descLine[0]
        self.cGrant = descLine[1]
        self.cDeny = descLine[2]
