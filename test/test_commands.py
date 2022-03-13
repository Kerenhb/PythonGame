from unittest import TestCase

from Game.Room import Room
from Game.Player import Player
from Game.Collection import Collection
from Game.Items import BOOK
from Game.Commands import *

class TestCommands(TestCase):
  def test_enter(self):
    testRoom = Room("Name", "Description")
    self.assertEqual(
        f'You enter Name\n'
        +'\033[1mName\033[0m\nDescription', enter(testRoom))

  def test_retrieveItem_existing(self):
    player = Player("Player")
    draw = Collection("Draw").add(BOOK)
    retrieveItem(player, BOOK, draw)

    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("are holding: Book", player.str_inventory())

  def test_retrieveItem_missing(self):
    player = Player("Player")
    draw = Collection("Draw")
    retrieveItem(player, BOOK, draw)

    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_placeItem_existing(self):
    player = Player("Player").pickUp(BOOK)
    draw = Collection("Draw")
    placeItem(player, BOOK, draw)

    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw contains: Book", str(draw))

  def test_placeItem_missing(self):
    player = Player("Player")
    draw = Collection("Draw")
    placeItem(player, BOOK, draw)

    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw is empty", str(draw))
