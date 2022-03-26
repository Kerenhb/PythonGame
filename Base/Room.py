from Base.Storage import Storage
from Game.Items import BOOK

class Room:
  def __init__(self, name, description, storage=None, north=None, south=None, west=None, east=None):
    # Note storage names should be in lower case and a single word to make commands easier
    if storage is None:
      storage = {}

    self.name = name
    self.description = description
    self.storage = storage

    self.north = north
    self.south = south
    self.west = west
    self.east = east

  def set_north(self, room):
    self.north = room

  def set_south(self, room):
    self.south = room

  def set_west(self, room):
    self.west = room

  def set_east(self, room):
    self.east = room

  def str_adjacent(self):
    output = ""
    if self.north: output += f'\nNorth is {self.north.name}'
    if self.south: output += f'\nSouth is {self.south.name}'
    if self.west: output += f'\nWest is {self.west.name}'
    if self.east: output += f'\nEast is {self.east.name}'
    return output

  def str_storage(self):
    output = ""
    for name, items in self.storage.items():
      output += f'\n{items.toString(name)}'
    return output

  def __str__(self):
    return f'\033[1m{self.name}\033[0m\n{self.description}{self.str_storage()}{self.str_adjacent()}'

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bedroomDescription = "The white walls of the room are matched by the color of the furniture.\
 A rack of shoes sits neatly in one corner and the dresser and bedside table are clear of dust."
  bedroom = Room("Julianna's Bedroom", bedroomDescription,
                 {"dresser": Storage([BOOK]), "bedside table": Storage()})

  hallway = Room("The Hallway", "An empty hallway", {}, bedroom)
  bedroom.set_south(hallway)

  print(bedroom)
  print("\n")
  print(hallway)
