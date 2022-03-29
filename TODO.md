# Create
* Create North/South and east/west (static) link functions, so it updates both rooms in one line,
every time.
* Could make it so that every door can be locked 
  * Maybe add a link class or something to ensure that both sides are unlocked
  * not really relevant for getting out though, so could just make an exception for the front door

## Create my game (separate file)
* Add an objective, mentioned at the start with a command to remind you of it
  * perhaps it could change as you progress (hints?)
* With rooms, etc
* Add object interactions as needed
* Win condition ideas 
  * e.g. bookshelf contains book
  * Player is in X location (could be outside the map)
  * player inventory contains an item / key
  * Win condition could be to get outside (check player location is outside, which will be a room)
    * and to do that you need to unlock a door (which needs a key, that could e hidden in a book that you need to examine).

# Misc Thoughts
* Could add Examine (x) - provides a specific description of something present in the room or that the player is carrying.

* How to do object interactions?
  * Could have different states within the room or object (e.g. door locked or not)
  * Could switch out the room entirely in the map (so the door is always unlocked there), but then 
  need to copy across the collections, etc

* What about "There is a book lying in the center of the bed."???
  * Maybe have subtypes for 'in' verses 'on'?
  * Or maybe could have a map of things in a room, with a description so
    * {BOOK, "There is a book lying in the center of the bed."} 

* Could add some sort of map?
