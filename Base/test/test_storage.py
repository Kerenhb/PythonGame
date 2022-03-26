from unittest import TestCase

from Base.Storage import Storage

class TestStorage(TestCase):
  def test_add(self):
    draw = Storage()
    draw.add("Pencil")

    shelf = Storage()
    shelf.add("Giraffe")

    self.assertEqual(["Pencil"], draw.items)
    self.assertEqual(["Giraffe"], shelf.items)

  def test_remove_existing(self):
    draw = Storage()
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.items)

    draw.remove("Draw", "Pencil")
    self.assertEqual([], draw.items)

  def test_ignore_remove_non_existing(self):
    draw = Storage()
    draw.add("Pencil")
    self.assertEqual(["Pencil"], draw.items)

    try:
      draw.remove("Draw", "Ruler")
    except Exception as e:
      self.assertEqual("Draw does not contain Ruler", str(e))

    self.assertEqual(["Pencil"], draw.items)

  def test_str_empty(self):
    draw = Storage()
    self.assertEqual("The Draw is empty", draw.toString("Draw"))

  def test_str_non_empty(self):
    draw = Storage()
    draw.add("Pencil")
    draw.add("Comb")
    self.assertEqual("The Draw contains: Pencil, Comb", draw.toString("Draw"))
