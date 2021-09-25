# Create
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

* What about "There is a book lying in the center of the bed."???
  * Maybe have subtypes for 'in' verses 'on'?
  * Or maybe could have a map of things in a room, with a description so
    * {BOOK, "There is a book lying in the center of the bed."} 
