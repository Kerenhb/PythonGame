from Base.Commands import *
from Game.setup import setup

def parseCommand(command):
  if command == "north" or command == "n":
    moveNorth(player)
    return f'You move North and enter {player.location.name}'
  elif command == "south" or command == "s":
    moveSouth(player)
    return f'You move South and enter {player.location.name}'
  elif command == "west" or command == "w":
    moveWest(player)
    return f'You move West and enter {player.location.name}'
  elif command == "east" or command == "e":
    moveEast(player)
    return f'You move East and enter {player.location.name}'
  # elif command == "take" or command == "t":
  #   takeItem(player, item, collection)
  # elif command == "place" or command == "p":
  #   placeItem(player, item, collection)
  elif command == "look" or command == "l":
    return player.location
  elif command == "inventory" or command == "i":
    return player.str_inventory()
  elif command == "help" or command == "h":
    return helpText()
  else:
    return command + " is not a valid command\n" + helpText()

if __name__ == "__main__":
  player = setup("Keren")

  while True:
    print(player.location)
    command = input("\nWhat do you want to do?")

    try:
      command = command.lower()
      if command == "quit" or command == "q" or command == "exit":
        print("Quiting the game")
        break

      print(parseCommand(command))
    except Exception as e:
      print(e)

  # print(move("South", player))

