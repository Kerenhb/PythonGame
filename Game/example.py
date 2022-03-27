from Base.Storage import Storage
from Base.Room import Room
from Base.Player import Player
from Game.Items import BOOK

def setup(playerName):
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  # Bedroom
  bedroom = Room(playerName + "'s Bedroom", "The white walls of the room are " +
                  "matched by the color of the furniture.\n A rack of shoes sits " +
                 "neatly in one corner and the dresser and bedside table are " +
                 "clear of dust.", {"dresser": Storage(), "table": Storage([BOOK])})

  # Hallway
  hallway = Room("The Hallway", "An empty hallway")

  # Connections
  bedroom.set_south(hallway)
  hallway.set_north(bedroom)

  # Player
  player = Player(playerName, bedroom)
  return player

def winCondition(player):
  return BOOK in player.inventory
