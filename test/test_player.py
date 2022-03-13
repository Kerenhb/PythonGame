from unittest import TestCase

from Game.Player import Player

class TestPlayer(TestCase):
  def test_str_empty(self):
    player = Player("Player")
    self.assertEqual("You are Player and your pockets are empty", str(player))

  def test_str_non_empty(self):
    player = Player("Player")
    player.pickUp("Pencil")
    player.pickUp("Comb")
    self.assertEqual("You are Player and are holding: Pencil, Comb", str(player))

  def test_pickUp(self):
    player = Player("Player")
    player.pickUp("Phone")

    self.assertEqual("are holding: Phone", player.str_inventory())

  def test_drop_existing(self):
    player = Player("Player")
    player.pickUp("Phone")
    self.assertEqual("are holding: Phone", player.str_inventory())

    player.drop("Phone")
    self.assertEqual("your pockets are empty", player.str_inventory())

  def test_ignore_drop_non_existing(self):
    player = Player("Player")
    player.pickUp("Phone")
    self.assertEqual("are holding: Phone", player.str_inventory())

    try:
      player.drop("Pen")
    except Exception as e:
      self.assertEqual("Your not holding Pen", str(e))

    self.assertEqual("are holding: Phone", player.str_inventory())
