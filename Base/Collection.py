from Game.Items import BOOK

class Collection:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add(self, item):
    self.items.append(item)
    return self

  def remove(self, item):
    if(self.items.__contains__(item)):
      self.items.remove(item)
    else:
      raise Exception(f'{self.name} does not contain {item}')
    return self

  def __str__(self):
    if(len(self.items)):
      return f'The {self.name} contains: {", ".join(self.items)}'
    else:
      return f'The {self.name} is empty'

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bookshelf = Collection("Bookshelf")
  print(bookshelf)
  bookshelf.add(BOOK)
  print(bookshelf)
