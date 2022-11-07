class Battle:
  def __init__(self, me, opponent):
    self.me = me
    self.opponent = opponent

  def other(self, player):
    if player == self.me:
      return self.opponent
    elif player == self.opponent:
      return self.me
      
  def attack(self, player):
    damage = player.ATK - (0.5 * self.other(player).DEF)
    self.other(player).takeDamage(damage)
    return player.name + " attacked and dealt " + str(damage) + " damage to " + self.other(player).name + "!"

  def specialAttack(self, player):
    if player.major == "Math":
      print(player.name + " explained how to do double integrals!")
      self.other(player).takeDamage(25)
      print(player.other.name + " is very confused...")
  
  def useItem(self, player, item):
    if item.effect == "heal":
      player.heal(item.value)
    elif item.effect == "damage":
      self.other(player).takeDamage(item.value)
    elif item.effect == "atkboost":
      player.ATK += item.value

  def myTurn(self):
    return 0
    
  def yourTurn(self): 
    self.opponent.attack(self, self.me)

  def checkBattleOver(self):
    if self.me.HP == 0:
      self.endBattle()
      return "Defeat"
    if self.opponent.HP == 0:
      self.endBattle()
      return "Victory"
    else:
      return "No"
  
  def endBattle(self):
    self.me.ATK = self.me.maxATK
    self.me.DEF = self.me.maxDEF
    self.me.LCK = self.me.maxLCK
    self.opponent.ATK = self.opponent.maxATK
    self.opponent.DEF = self.opponent.maxDEF
    self.opponent.LCK = self.opponent.maxLCK



  
  

