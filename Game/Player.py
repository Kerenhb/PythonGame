class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []

  def pickUp(self, object):
    self.inventory.append(object)
    return self

  def drop(self, item):
    if(self.inventory.__contains__(item)):
      self.inventory.remove(item)
    else:
      raise Exception(f'Your not holding {item}')

  def str_inventory(self):
    if(len(self.inventory)):
      return f'are holding: {", ".join(self.inventory)}'
    else:
      return f'your pockets are empty'

  def __str__(self):
    return f'You are {self.name} and {self.str_inventory()}'

if __name__ == "__main__":
  player = Player("Keren")
  print(player)
  player.pickUp("Phone")
  print(player)
