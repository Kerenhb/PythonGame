from Base.Room import Room

class Player:
  def __init__(self, name, location):
    self.name = name
    self.location = location
    self.inventory = []

  def pickUp(self, object):
    self.inventory.append(object)
    return self

  def drop(self, item):
    if(self.inventory.__contains__(item)):
      self.inventory.remove(item)
    else:
      raise Exception(f'Your not holding {item}')

  def move(self, newLocation):
    self.location = newLocation
    return self

  def str_inventory(self):
    if(len(self.inventory)):
      return f'you\'re holding: {", ".join(self.inventory)}'
    else:
      return f'your pockets are empty'

  def __str__(self):
    return f'You are {self.name}, {self.str_inventory()} and you\'re currently ' \
           f'in {self.location.name}'

if __name__ == "__main__":
  bedroom = Room("Bedroom", "An empty bedroom")
  player = Player("Keren", bedroom)
  print(player)
  player.pickUp("Phone")
  print(player)
