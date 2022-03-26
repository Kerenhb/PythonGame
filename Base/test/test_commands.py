from unittest import TestCase

from Base.Room import Room
from Base.Player import Player
from Base.Collection import Collection
from Base.Commands import *
from Game.Items import BOOK

class TestCommands(TestCase):
  def test_move_north_existing(self):
    testRoom2 = Room("testRoom2", "Description")
    testRoom1 = Room("testRoom1", "Description", None, testRoom2)
    player = Player("Player", testRoom1)

    moveNorth(player)
    self.assertEqual(testRoom2, player.location)

  def test_move_north_missing(self):
    testRoom1 = Room("testRoom1", "Description")
    player = Player("Player", testRoom1)

    try:
      moveNorth(player)
    except Exception as e:
      self.assertEqual('You can not go North', str(e))

    self.assertEqual(testRoom1, player.location)

  def test_move_south_existing(self):
    testRoom2 = Room("testRoom2", "Description")
    testRoom1 = Room("testRoom1", "Description", None, None, testRoom2)
    player = Player("Player", testRoom1)

    moveSouth(player)
    self.assertEqual(testRoom2, player.location)

  def test_move_south_missing(self):
    testRoom1 = Room("testRoom1", "Description")
    player = Player("Player", testRoom1)

    try:
      moveSouth(player)
    except Exception as e:
      self.assertEqual('You can not go South', str(e))

    self.assertEqual(testRoom1, player.location)

  def test_move_west_existing(self):
    testRoom2 = Room("testRoom2", "Description")
    testRoom1 = Room("testRoom1", "Description", None, None, None, testRoom2)
    player = Player("Player", testRoom1)

    moveWest(player)
    self.assertEqual(testRoom2, player.location)

  def test_move_west_missing(self):
    testRoom1 = Room("testRoom1", "Description")
    player = Player("Player", testRoom1)

    try:
      moveWest(player)
    except Exception as e:
      self.assertEqual('You can not go West', str(e))

    self.assertEqual(testRoom1, player.location)

  def test_move_east_existing(self):
    testRoom2 = Room("testRoom2", "Description")
    testRoom1 = Room("testRoom1", "Description", None, None, None, None, testRoom2)
    player = Player("Player", testRoom1)

    moveEast(player)
    self.assertEqual(testRoom2, player.location)

  def test_move_east_missing(self):
    testRoom1 = Room("testRoom1", "Description")
    player = Player("Player", testRoom1)

    try:
      moveEast(player)
    except Exception as e:
      self.assertEqual('You can not go East', str(e))

    self.assertEqual(testRoom1, player.location)

  def test_retrieveItem_existing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw").add(BOOK)

    takeItem(player, BOOK, draw)
    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("you're holding: Book", player.str_inventory())

  def test_retrieveItem_missing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw")

    try:
      takeItem(player, BOOK, draw)
    except Exception as e:
      self.assertEqual('Draw does not contain Book', str(e))

    self.assertEqual("The Draw is empty", str(draw))
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_placeItem_existing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom).take(BOOK)
    draw = Collection("Draw")

    placeItem(player, BOOK, draw)
    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw contains: Book", str(draw))

  def test_placeItem_missing(self):
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)
    draw = Collection("Draw")

    try:
      placeItem(player, BOOK, draw)
    except Exception as e:
      self.assertEqual('Your not holding Book', str(e))

    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The Draw is empty", str(draw))
