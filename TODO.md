# Create
## Main Game Class
* Complete the basic example from https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f
  * Add object interactions as needed

## Create my game
* With rooms, etc
* Add object interactions as needed
* Win condition ideas 
  * e.g. bookshelf contains book
  * Player is in X location (could be outside the map)
  * player inventory contains an item / key
  * Put into a function so it's easier to change later

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
