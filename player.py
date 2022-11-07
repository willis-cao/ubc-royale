import random
import math


class Player:

    def __init__(self, name, major, type, bio):
      self.name = name
      self.major = major
      self.type = type
      self.bio = bio
      self.items = []
      self.level = 1
      self.maxHP = 0
      self.maxATK = 0
      self.maxDEF = 0
      self.maxLCK = 0
      self.setStats()
      self.HP = self.maxHP
      self.ATK = self.maxATK
      self.DEF = self.maxDEF
      self.LCK = self.maxLCK

    def setStats(self):
      if self.type == "Attacker":
        self.maxHP = 100
        self.maxATK = 25
        self.maxDEF = 15
        self.maxLCK = 20
      elif self.type == "Defender":
        self.maxHP = 100
        self.maxATK = 15
        self.maxDEF = 25
        self.maxLCK = 20
      elif self.type == "God":
        self.maxHP = 1000
        self.maxATK = 100
        self.maxDEF = 100
        self.maxLCK = 100
      elif self.type == "Tree":
        self.maxHP = 200
        self.maxATK = 15
        self.maxDEF = 20
        self.maxLCK = 0
      elif self.type == "Sleep Deprived":
        self.maxHP = 50
        self.maxATK = 30
        self.maxDEF = 10
        self.maxLCK = 20
      self.HP = self.maxHP
      self.ATK = self.maxATK
      self.DEF = self.maxDEF
      self.LCK = self.maxLCK
  
    def levelUp(self):
        self.level += 1
        self.maxHP += random.randint(1, 3)
        self.maxATK += random.randint(1, 3)
        self.maxDEF += random.randint(1, 3)
        self.maxLCK += random.randint(1, 3)

    def heal(self, value):
        if self.HP + value > self.maxHP:
            self.HP = self.maxHP
        else:
            self.HP += value

    def takeDamage(self, value):
        if self.HP - value < 0:
            self.HP = 0
        else:
            self.HP -= value

    def returnItemList(self):
        for i in self.items:
            print(i.name)

    def healthPercent(self):
        return math.floor(100 * (self.HP / self.maxHP))

    def setLevel(self, level):
        self.level = level
