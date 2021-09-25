# Create
## Object
* File of string literals
* e.g. BOOK = "Book", then can use them everywhere

## Collection
* Has a name and list of objects
* Can add or remove objects
  * with the obvious checks  
* Has a str function that prints out
  * "The Bookshelf is empty" or "The Bookshelf contains a Book (, xxx and yyy)"
* Add a list of collections to a room and add it to what's printed out when you enter it, unless empty

## Player
* Name?
* Inventory (collection of objects?)
* Current Room (or could go in the Map)

## Map
* Add a basic map, where you can define what rooms are next to each other
    * Perhaps a basic 2d array type thing?
* Add ability to move in each compass direction (N/E/W/S), obviously first checking there is a room there
  * Part of Room, Map or Person?

## Main Game Class
* Sets up the Rooms, Map, etc
* As well as the main game loop
* Creates a win condition that's checked every time you enter the loop (e.g. bookshelf contains book)

# Misc Thoughts
* How to do object interactions?
  * Could have different states within the room or object (e.g. door locked or not)
  * Could switch out the room entirely in the map (so the door is always unlocked there), but then 
  need to copy across the collections, etc
