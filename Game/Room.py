class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f'\033[1m{self.name}\033[0m\n{self.description}'

  def enter(self):
    print(self)

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bedroomDescription = "The white walls of the room are matched by the color of the furniture.\
 A rack of shoes sits neatly in one corner and the dresser and bedside table are clear of dust."
  bedroom = Room("Julianna's Bedroom", bedroomDescription)

  bedroom.enter()



