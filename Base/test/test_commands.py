from unittest import TestCase

from Base.Room import Room
from Base.Player import Player
from Base.Collection import Collection
from Base.Commands import *
from Game.Items import BOOK

class TestCommands(TestCase):
  def test_move_existing(self):
    testRoom2 = Room("testRoom2", "Description")
    testRoom1 = Room("testRoom1", "Description", None, testRoom2)
    player = Player("Player", testRoom1)

    self.assertEqual(
        f'You move North and enter testRoom2\n'
        +'\033[1mtestRoom2\033[0m\nDescription', move("North", player))

  def test_move_missing(self):
    testRoom1 = Room("testRoom1", "Description")
    player = Player("Player", testRoom1)

    self.assertEqual('You can not go North', str(move("North", player)))

  def test_retrieveItem_existing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw").add(BOOK)

    retrieveItem(player, BOOK, draw)
    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("you're holding: Book", player.str_inventory())

  def test_retrieveItem_missing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw")

    self.assertEqual('Draw does not contain Book', str(retrieveItem(player, BOOK, draw)))
    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_placeItem_existing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom).pickUp(BOOK)
    draw = Collection("Draw")

    placeItem(player, BOOK, draw)
    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw contains: Book", str(draw))

  def test_placeItem_missing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw")

    self.assertEqual('Your not holding Book', str(placeItem(player, BOOK, draw)))
    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw is empty", str(draw))
