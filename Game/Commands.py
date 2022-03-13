def enter(room):
  return "You enter " + room.name + "\n" + str(room)

def move(direction, currentRoom):
  newRoom= ""

  try:
    if direction == "North": newRoom = __moveNorth(currentRoom)
    if direction == "South": newRoom = __moveSouth(currentRoom)
    if direction == "West": newRoom = __moveWest(currentRoom)
    if direction == "East": newRoom = __moveEast(currentRoom)
  except Exception as e:
    print(e)
    newRoom = currentRoom

  enter(newRoom)
  return newRoom

def __moveNorth(currentRoom):
  if currentRoom.north:
    print("You move North")
    return currentRoom.north
  else:
    raise Exception('You can not go North')

def __moveSouth(currentRoom):
  if currentRoom.south:
    print("You move South")
    return currentRoom.south
  else:
    raise Exception('You can not go South')

def __moveWest(currentRoom):
  if currentRoom.west:
    print("You move West")
    return currentRoom.west
  else:
    raise Exception('You can not go West')

def __moveEast(currentRoom):
  if currentRoom.east:
    print("You move East")
    return currentRoom.east
  else:
    raise Exception('You can not go East')

def retrieveItem(player, item, collection):
  try:
    collection.remove(item)
    player.pickUp(item)
  except Exception as e:
    print(e)

def placeItem(player, item, collection):
  try:
    player.drop(item)
    collection.add(item)
  except Exception as e:
    print(e)

