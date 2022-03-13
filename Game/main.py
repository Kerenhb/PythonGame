from Game.Collection import Collection
from Game.Room import Room
from Game.Commands import *
from Game.Items import BOOK

def setup():
  bedroomDescription = "The white walls of the room are matched by the color of the furniture.\
  A rack of shoes sits neatly in one corner and the dresser and bedside table are clear of dust."
  dresser = Collection("Dresser").add(BOOK)
  table = Collection("Bedside table")
  bedroom = Room("Julianna's Bedroom", bedroomDescription, [dresser, table])
  return bedroom

if __name__ == "__main__":
  start = setup()
  print(enter(start))
