from Base.Commands import *
from Game.example import setup, winCondition

def parseCommand(command):
  if "north" in command or "n" in command:
    moveNorth(player)
    return f'You move North and enter {player.location.name}'
  elif "south" in command or "s" in command:
    moveSouth(player)
    return f'You move South and enter {player.location.name}'
  elif "west" in command or "w" in command:
    moveWest(player)
    return f'You move West and enter {player.location.name}'
  elif "east" in command or "e" in command:
    moveEast(player)
    return f'You move East and enter {player.location.name}'
  elif command[0] == "take" or command[0] == "t":
    if len(command) > 2:
      # assuming command[2] is 'from'
      takeItem(player, command[1], command[3])
    else:
      takeAnyItem(player, command[1])
    return f'You take {command[1]}'
  elif command[0] == "place" or command[0] == "p":
    # assuming command[2] is 'in/on'
    placeItem(player, command[1], command[3])
    return f'You place {command[1]}'
  elif "look" in command or "l" in command:
    return player.location
  elif "inventory" in command or "i" in command:
    return player.str_inventory()
  elif "help" in command or "h" in command:
    return helpText()
  else:
    return "'" + " ".join(command) + "' is not a valid command\n" + helpText()

if __name__ == "__main__":
  player, livingRoom = setup("Keren")

  while True:
    print(player.location)
    command = input("\nWhat do you want to do?")

    try:
      command = command.lower().split()
      if command == ["quit"] or command == ["q"] or command == ["exit"]:
        print("Quiting the game")
        break

      print(parseCommand(command))
      if winCondition(livingRoom):
        print(f'\033[1mYou win the game!\033[0m')
        break

    except Exception as e:
      print(e)

