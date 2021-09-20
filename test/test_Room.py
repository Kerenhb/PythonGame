from unittest import TestCase

from Game.Room import Room

class TestRoom(TestCase):
  def test_enter(self):
    testRoom = Room("Name", "Description")
    self.assertEqual(testRoom.name, "Name")
    self.assertEqual(testRoom.description, "Description")
