from unittest import TestCase

from Game.Collection import Collection

class TestCollection(TestCase):
  def test_add(self):
    draw = Collection("Draw")
    draw.add("Pencil")

    shelf = Collection("Shelf")
    shelf.add("Giraffe")

    self.assertEqual(["Pencil"], draw.items)
    self.assertEqual(["Giraffe"], shelf.items)

  def test_remove_existing(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.items)

    draw.remove("Pencil")
    self.assertEqual([], draw.items)

  def test_ignore_remove_non_existing(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.items)

    try:
      draw.remove("Ruler")
    except Exception as e:
      self.assertEqual("Draw does not contain Ruler", str(e))

    self.assertEqual(["Pencil"], draw.items)

  def test_str_empty(self):
    draw = Collection("Draw")
    self.assertEqual("The Draw is empty", str(draw))

  def test_str_non_empty(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    draw.add("Comb")
    self.assertEqual("The Draw contains: Pencil, Comb", str(draw))
