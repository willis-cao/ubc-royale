import random
class Place:

  def __init__(self, name, specialItems, people):
      self.name = name
      self.specialItems = specialItems
      self.people = people

  # def getName(self):
  #   return self.name

  # def getSpecialItems(self):
  #   return self.specialItems

  # def getPeople(self):
  #   return self.people

  def addPerson(self, player):
     self.people.append(player)

  def addSpecialItem(self, item):
     self.specialItems.append(item)

  def dropItem(self, player):
    randNum = random.randint(1, 100)
    print(randNum)
    if randNum <= player.LCK:
      item = random.choice(self.specialItems)
      player.items.append(item)
      print("You found an item: " + item.name + "!")
      
    # boolList = [True, False, False, False, False]
    # w1 = 20 + (player.LCK/10)
    # w2 = (100 - w1)/4
    # gettingItem = random.choices(boolList, weights = (w1, w2, w2, w2, w2), k=1)
    # print(gettingItem)
    # if gettingItem:
    #   item = random.choice(self.specialItems)
    #   player.items.append(item)
    # else:
    #   print("no items added")
    