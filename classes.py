class Protagonist:
       def __init__(self, img):
              self.img = img
       
       def setName(self, name):
              self.name = name
       

class NPC:
       def __init__(self, name, img):
              self.name = name
              self.img = img
              self.affectionLevel = 0
       
       def increaseAffectionLevel(self, amount=1):
              self.affectionLevel = self.affectionLevel + amount
              
       def decreaseAffectionLevel(self, amount=1):
              self.affectionLevel = self.affectionLevel - amount
       