from unittest import TestCase

from Game.Player import Player

class TestPlayer(TestCase):
  def test_str_empty(self):
    player1 = Player("Player1")
    self.assertEqual("You are Player1 and your pockets are empty", str(player1))

  def test_str_non_empty(self):
    player1 = Player("Player1")
    player1.pickUp("Pencil")
    player1.pickUp("Comb")
    self.assertEqual("You are Player1 and are holding: Pencil, Comb", str(player1))

  def test_pickUp(self):
    player1 = Player("Player1")
    player1.pickUp("Phone")

    player2 = Player("Player2")
    player2.pickUp("Pen")

    self.assertEqual("are holding: Phone", player1.str_inventory())
    self.assertEqual("are holding: Pen", player2.str_inventory())

  def test_drop_existing(self):
    player1 = Player("Player1")
    player1.pickUp("Phone")
    self.assertEqual("are holding: Phone", player1.str_inventory())

    player1.drop("Phone")
    self.assertEqual("your pockets are empty", player1.str_inventory())

  def test_ignore_drop_non_existing(self):
    player1 = Player("Player1")
    player1.pickUp("Phone")
    self.assertEqual("are holding: Phone", player1.str_inventory())

    player1.drop("Pen")
    self.assertEqual("are holding: Phone", player1.str_inventory())
