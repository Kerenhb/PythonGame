def moveNorth(player):
  if player.location.north:
    player.move(player.location.north)
  else:
    raise Exception('You can not go North')

def moveSouth(player):
  if player.location.south:
    player.move(player.location.south)
  else:
    raise Exception('You can not go South')

def moveWest(player):
  if player.location.west:
    player.move(player.location.west)
  else:
    raise Exception('You can not go West')

def moveEast(player):
  if player.location.east:
    player.move(player.location.east)
  else:
    raise Exception('You can not go East')

def takeAnyItem(player, item):
  for storageName, storage in player.location.storage.items():
    if item in storage.items:
      storage.remove(storageName, item)
      player.take(item)
      return

  raise Exception(item + " is not in this room")

def takeItem(player, item, storageName):
  possibleStorageNames = player.location.storage.keys()
  if storageName in possibleStorageNames:
    player.location.storage[storageName].remove(storageName, item)
    player.take(item)
  else:
    raise Exception(storageName + " is not in this room")

def placeItem(player, item, storageName):
  possibleStorageNames = player.location.storage.keys()
  if storageName in possibleStorageNames:
    player.drop(item)
    player.location.storage[storageName].add(item)
  else:
    raise Exception(storageName + " is not in this room")

def helpText():
  return "The commands you can use are (case-insensitive):\n" \
         "* North (n), South (s), East (e) or West (w) - To move in those directions\n" \
         "* Take (t) ITEM, Take (t) ITEM from STORAGE - to take items" \
         "* Place (p) ITEM in/on STORAGE - To place items\n" \
         "* Look (l) - Repeats description of current room\n" \
         "* Inventory (i) - Tells you what your holding\n" \
         "* Help (h) - Shows this help text\n" \
         "* Quit (q) or Exit - Quits the game"
