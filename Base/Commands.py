def move(direction, player):
  try:
    if direction == "North": __moveNorth(player)
    if direction == "South": __moveSouth(player)
    if direction == "West": __moveWest(player)
    if direction == "East": __moveEast(player)

    return f'You move {direction} and enter {player.location.name}\n{str(player.location)}'
  except Exception as e:
    return e

def __moveNorth(player):
  if player.location.north:
    player.move(player.location.north)
  else:
    raise Exception('You can not go North')

def __moveSouth(player):
  if player.location.south:
    player.move(player.location.south)
  else:
    raise Exception('You can not go South')

def __moveWest(player):
  if player.location.west:
    player.move(player.location.west)
  else:
    raise Exception('You can not go West')

def __moveEast(player):
  if player.location.east:
    player.move(player.location.east)
  else:
    raise Exception('You can not go East')

def retrieveItem(player, item, collection):
  try:
    collection.remove(item)
    player.pickUp(item)
  except Exception as e:
    return e

def placeItem(player, item, collection):
  try:
    player.drop(item)
    collection.add(item)
  except Exception as e:
    return e

