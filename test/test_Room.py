from unittest import TestCase

from Game.Room import Room
from Game.Collection import Collection

class TestRoom(TestCase):
  def test_str_storage_0(self):
    testRoom = Room("Name", "Description", [])
    self.assertEqual("", testRoom.str_storage())

  def test_str_storage_1(self):
    testCollection = Collection("Collection")
    testRoom = Room("Name", "Description", [testCollection])
    self.assertEqual(f'\n{str(testCollection)}', testRoom.str_storage())

  def test_str_storage_many(self):
    testCollection1 = Collection("Collection1")
    testCollection2 = Collection("Collection2")
    testCollection3 = Collection("Collection3")
    testRoom = Room("Name", "Description", [testCollection1, testCollection2, testCollection3])
    self.assertEqual(f'\n{str(testCollection1)}\n{str(testCollection2)}\n{str(testCollection3)}', testRoom.str_storage())

  def test_str(self):
    testCollection = Collection("Collection")
    testRoom = Room("Name", "Description", [testCollection])
    self.assertEqual(f'\033[1mName\033[0m\nDescription\n{str(testCollection)}', str(testRoom))

  def test_str_no_storage(self):
    testRoom = Room("Name", "Description")
    self.assertEqual("\033[1mName\033[0m\nDescription", str(testRoom))

  def test_str_with_rooms(self):
    testRoom1 = Room("Name1", "Description1")
    testRoom2 = Room("Name2", "Description2")
    testRoom3 = Room("Name3", "Description3")
    testRoom1.set_south(testRoom2)
    testRoom1.set_west(testRoom3)

    self.assertEqual(
        "\033[1mName1\033[0m\nDescription1"
        "\n\nSouth is Name2"
        "\nWest is Name3",
        str(testRoom1))
