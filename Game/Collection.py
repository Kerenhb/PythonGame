from Game.Objects import BOOK

class Collection:
  def __init__(self, name):
    self.name = name
    self.objects = []

  def add(self, object):
    self.objects.append(object)

  def remove(self, object):
    if(self.objects.__contains__(object)):
      self.objects.remove(object)
    else:
      print(f'{self.name} does not contain {object}')

  def __str__(self):
    if(len(self.objects)):
      return f'The {self.name} contains: {", ".join(self.objects)}'
    else:
      return f'The {self.name} is empty'

if __name__ == "__main__":
  # Example taken from: https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

  bookshelf = Collection("Bookshelf")
  print(bookshelf)
  bookshelf.add(BOOK)
  print(bookshelf)
