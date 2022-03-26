from unittest import TestCase

from Base.Room import Room
from Base.Storage import Storage

class TestRoom(TestCase):
  def test_str_storage_0(self):
    testRoom = Room("Name", "Description")
    self.assertEqual("", testRoom.str_storage())

  def test_str_storage_1(self):
    testStorage = Storage()
    testRoom = Room("Name", "Description", {"storage": testStorage})
    self.assertEqual(f'\n{testStorage.toString("storage")}', testRoom.str_storage())

  def test_str_storage_many(self):
    testStorage1 = Storage()
    testStorage2 = Storage()
    testStorage3 = Storage()
    testRoom = Room("Name", "Description",
                    {"Storage1": testStorage1, "Storage2": testStorage2, "Storage3": testStorage3})
    self.assertEqual(f'\n{testStorage1.toString("Storage1")}'
                     f'\n{testStorage2.toString("Storage2")}'
                     f'\n{testStorage3.toString("Storage3")}',
                     testRoom.str_storage())

  def test_str(self):
    testStorage = Storage()
    testRoom = Room("Name", "Description", {"storage": testStorage})
    self.assertEqual(f'\033[1mName\033[0m\nDescription\n{testStorage.toString("storage")}', str(testRoom))

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
        "\nSouth is Name2"
        "\nWest is Name3",
        str(testRoom1))
