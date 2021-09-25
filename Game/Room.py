from Game.Collection import Collection
from Game.Objects import BOOK

class Room:
  def __init__(self, name, description, storage=None):
    if storage is None:
      storage = []

    self.name = name
    self.description = description
    self.storage = storage

  def enter(self):
    print(self) # Consider making this pure?

  def str_storage(self):
    output = ""
    for collection in self.storage:
      output += f'\n{str(collection)}'
    return output

  def __str__(self):
    return f'\033[1m{self.name}\033[0m\n{self.description}{self.str_storage()}'

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bedroomDescription = "The white walls of the room are matched by the color of the furniture.\
 A rack of shoes sits neatly in one corner and the dresser and bedside table are clear of dust."
  dresser = Collection("Dresser")
  bedroom = Room("Julianna's Bedroom", bedroomDescription, [dresser, Collection("Bedside table")])
  dresser.add(BOOK)

  bedroom.enter()
