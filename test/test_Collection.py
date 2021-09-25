from unittest import TestCase

from Game.Collection import Collection

class TestCollection(TestCase):
  def test_add(self):
    draw = Collection("Draw")
    draw.add("Pencil")

    shelf = Collection("Shelf")
    shelf.add("Giraffe")

    self.assertEqual(["Pencil"], draw.objects)
    self.assertEqual(["Giraffe"], shelf.objects)

  def test_remove_existing(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.objects)

    draw.remove("Pencil")
    self.assertEqual([], draw.objects)

  def test_ignore_remove_non_existing(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.objects)

    draw.remove("Ruler")
    self.assertEqual(["Pencil"], draw.objects)

  def test_str_empty(self):
    draw = Collection("Draw")
    self.assertEqual("The Draw is empty", str(draw))

  def test_str_non_empty(self):
    draw = Collection("Draw")
    draw.add("Pencil")
    draw.add("Comb")
    self.assertEqual("The Draw contains: Pencil, Comb", str(draw))
