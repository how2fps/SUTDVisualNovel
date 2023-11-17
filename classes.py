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
       
       def increaseAffectionLevel(self):
              self.affectionLevel = self.affectionLevel + 1
              
       def decreaseAffectionLevel(self):
              self.affectionLevel = self.affectionLevel - 1
       