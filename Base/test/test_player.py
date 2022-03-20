from unittest import TestCase

from Base.Player import Player
from Base.Room import Room

class TestPlayer(TestCase):
  def test_str_empty(self):
    room = Room("Room", "An empty room")
    player = Player("Player", room)
    self.assertEqual("You are Player, your pockets are empty and you're currently in Room",
                     str(player))

  def test_str_non_empty(self):
    room = Room("Room", "An empty room")
    player = Player("Player", room)
    player.pickUp("Pencil")
    player.pickUp("Comb")
    self.assertEqual("You are Player, you're holding: Pencil, Comb and you're currently in Room",
                     str(player))

  def test_pickUp(self):
    room = Room("Room", "An empty room")
    player = Player("Player", room)
    player.pickUp("Phone")

    self.assertEqual("you're holding: Phone", player.str_inventory())

  def test_drop_existing(self):
    room = Room("Room", "An empty room")
    player = Player("Player", room)
    player.pickUp("Phone")
    self.assertEqual("you're holding: Phone", player.str_inventory())

    player.drop("Phone")
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_ignore_drop_non_existing(self):
    room = Room("Room", "An empty room")
    player = Player("Player", room)
    player.pickUp("Phone")
    self.assertEqual("you're holding: Phone", player.str_inventory())

    try:
      player.drop("Pen")
    except Exception as e:
      self.assertEqual("Your not holding Pen", str(e))

    self.assertEqual("you're holding: Phone", player.str_inventory())

  def test_move(self):
    room1 = Room("Room1", "An empty room")
    player = Player("Player", room1)
    self.assertEqual("You are Player, your pockets are empty and you're currently in Room1",
                     str(player))

    room2 = Room("Room2", "An empty room")
    player.move(room2)
    self.assertEqual("You are Player, your pockets are empty and you're currently in Room2",
                     str(player))
