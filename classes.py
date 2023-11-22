class Protagonist:
       def __init__(self, img, name):
              self.img = img
              self.name = name
       
       def setName(self, name):
              self.name = name

       def getName(self):
              return self.name
       

class NPC:
       def __init__(self, name, img=""):
              self.name = name
              self.img = img
              self.affectionLevel = 0
       
       def increaseAffectionLevel(self, amount=1):
              self.affectionLevel = self.affectionLevel + amount
              
       def decreaseAffectionLevel(self, amount=1):
              self.affectionLevel = self.affectionLevel - amount
       
       def getAffectionLevel(self):
              return self.affectionLevel