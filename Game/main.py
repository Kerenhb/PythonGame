from Base.Commands import *
from Game.setup import setup

def parseCommand(command):
  if command == ["north"] or command == ["n"]:
    moveNorth(player)
    return f'You move North and enter {player.location.name}'
  elif command == ["south"] or command == ["s"]:
    moveSouth(player)
    return f'You move South and enter {player.location.name}'
  elif command == ["west"] or command == ["w"]:
    moveWest(player)
    return f'You move West and enter {player.location.name}'
  elif command == ["east"] or command == ["e"]:
    moveEast(player)
    return f'You move East and enter {player.location.name}'
  elif command[0] == "take" or command[0] == "t":
    # assuming command[2] is 'from'
    takeItem(player, command[1], command[3])
    return f'You take {command[1]}'
  elif command[0] == "place" or command[0] == "p":
    # assuming command[2] is 'in/on'
    placeItem(player, command[1], command[3])
    return f'You place {command[1]}'
  elif command == ["look"] or command == ["l"]:
    return player.location
  elif command == ["inventory"] or command == ["i"]:
    return player.str_inventory()
  elif command == ["help"] or command == ["h"]:
    return helpText()
  else:
    return "'" + " ".join(command) + "' is not a valid command\n" + helpText()

if __name__ == "__main__":
  player = setup("Keren")

  while True:
    print(player.location)
    command = input("\nWhat do you want to do?")

    try:
      command = command.lower().split()
      if command == ["quit"] or command == ["q"] or command == ["exit"]:
        print("Quiting the game")
        break

      print(parseCommand(command))
    except Exception as e:
      print(e)

