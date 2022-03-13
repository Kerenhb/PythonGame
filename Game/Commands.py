def enter(room):
  return "You enter " + room.name + "\n" + str(room)

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

