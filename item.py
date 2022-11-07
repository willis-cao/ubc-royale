class Item:
  def __init__(self, name, effect, value):
    self.name = name
    self.effect = effect
    self.value = value

  def __str__(self):
    return self.name

  