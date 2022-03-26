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

def takeItem(player, item, collection):
  collection.remove(item)
  player.take(item)

def placeItem(player, item, collection):
  player.drop(item)
  collection.add(item)

def helpText():
  return "The commands you can use are (case-insensitive):\n" \
         "* North (n), South (s), East (e) or West (w) - To move in those directions\n" \
         "* Take (t), Place (p) - To take and place items\n" \
         "* Look (l) - Repeats description of current room\n" \
         "* Inventory (i) - Tells you what your holding\n" \
         "* Help (h) - Shows this help text\n" \
         "* Quit (q) or Exit - Quits the game"
