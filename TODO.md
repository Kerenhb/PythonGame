# Create
## Main Game Class
* Sets up the Rooms, Map, etc
* As well as the main game loop
  * Need to parse text commands (move, pick up, drop, look, etc) 
  * More commands here: http://www.mrbillsadventureland.com/howto/intfiction/textplay.htm
* Creates a win condition that's checked every time you enter the loop (e.g. bookshelf contains book)
* Add ability to move in each compass direction (N/E/W/S), obviously first checking there is a room there
* Current Room the player is in (or could go in the Player)

Then can complete the basic example from https://medium.com/coinmonks/how-to-create-your-own-text-adventure-12df36411b7f

# Misc Thoughts
* How to do object interactions?
  * Could have different states within the room or object (e.g. door locked or not)
  * Could switch out the room entirely in the map (so the door is always unlocked there), but then 
  need to copy across the collections, etc

* What about "There is a book lying in the center of the bed."???
  * Maybe have subtypes for 'in' verses 'on'?
  * Or maybe could have a map of things in a room, with a description so
    * {BOOK, "There is a book lying in the center of the bed."} 
