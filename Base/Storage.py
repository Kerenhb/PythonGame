from Game.Items import BOOK

class Storage:
  def __init__(self, items=None):
    if items is None:
      items = []

    self.items = items

  def add(self, item):
    self.items.append(item)
    return self

  def remove(self, name, item):
    if(self.items.__contains__(item)):
      self.items.remove(item)
    else:
      raise Exception(f'{name} does not contain {item}')
    return self

  def toString(self, name):
    if(len(self.items)):
      return f'The {name} contains: {", ".join(self.items)}'
    else:
      return f'The {name} is empty'

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bookshelf = Storage()
  print(bookshelf)
  bookshelf.add(BOOK)
  print(bookshelf)
