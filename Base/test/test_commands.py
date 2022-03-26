from unittest import TestCase

from Base.Room import Room
from Base.Player import Player
from Base.Storage import Storage
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

  def test_takeItem_existing(self):
    draw = Storage([BOOK])
    testRoom = Room("testRoom", "Description", {"draw": draw})
    player = Player("Player", testRoom)

    takeItem(player, BOOK, "draw")
    self.assertEqual("The draw is empty", draw.toString("draw"))
    self.assertEqual("you're holding: book", player.str_inventory())

  def test_takeItem_invalid_storage(self):
    draw = Storage([BOOK])
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom)

    try:
      takeItem(player, BOOK, "Draw")
    except Exception as e:
      self.assertEqual('Draw is not in this room', str(e))

    self.assertEqual("The Draw contains: book", draw.toString("Draw"))
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_takeItem_missing(self):
    draw = Storage()
    testRoom = Room("testRoom", "Description", {"draw": draw})
    player = Player("Player", testRoom)

    try:
      takeItem(player, BOOK, "draw")
    except Exception as e:
      self.assertEqual('draw does not contain book', str(e))

    self.assertEqual("The draw is empty", draw.toString("draw"))
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_placeItem_existing(self):
    draw = Storage()
    testRoom = Room("testRoom", "Description", {"draw": draw})
    player = Player("Player", testRoom).take(BOOK)

    placeItem(player, BOOK, "draw")
    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The draw contains: book", draw.toString("draw"))

  def test_placeItem_invalid_storage(self):
    draw = Storage()
    testRoom = Room("testRoom", "Description")
    player = Player("Player", testRoom).take(BOOK)

    try:
      placeItem(player, BOOK, "draw")
    except Exception as e:
      self.assertEqual('draw is not in this room', str(e))

    self.assertEqual("you're holding: book", player.str_inventory())
    self.assertEqual("The draw is empty", draw.toString("draw"))

  def test_placeItem_missing(self):
    draw = Storage()
    testRoom = Room("testRoom", "Description", {"draw": draw})
    player = Player("Player", testRoom)

    try:
      placeItem(player, BOOK, "draw")
    except Exception as e:
      self.assertEqual('Your not holding book', str(e))

    self.assertEqual("your pockets are empty", player.str_inventory())
    self.assertEqual("The draw is empty", draw.toString("draw"))
