# Author: David Miller | djm545
# Date: 5/24/23
# Purpose: A maze game using classes that act similarly to linked lists

from room import Room
from maze import Maze

def play(my_maze):
    # Play a game
    while not my_maze.atExit():
        # Get direction from user
        move = False # Presumes the move is not valid
        while not move: # Runs until move is valid
            print(f"{my_maze.getCurrent()}")
            direction = input("Enter direction to move north west east south restart")

            # Based on choice do what was asked.
            if direction == "north" or direction == "west" or direction == "east" or direction == "south":
                if direction == "north":
                    move = my_maze.moveNorth()
                elif direction == "east":
                    move = my_maze.moveEast()
                elif direction == "west":
                    move = my_maze.moveWest()
                elif direction == "South":
                    move = my_maze.moveSouth()
                    
                if move:
                    print(f"You went {direction}")
                else:
                    print("Direction invalid, try again.")
            elif direction == "restart":
                move = True # Breaks from the move loop to reprint the room description
                my_maze.reset()
                print("You went back to the start!")
            else:
                print("Invalid Entry")
    print("You found the exit!")


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
sRoom1 = Room("Room1")
sRoom2 = Room("Room2")
sRoom3 = Room("Room3")

# east, north
sRoom1.setEast(sRoom2)
sRoom2.setNorth(sRoom3)
SIMPLE_MAZE = Maze(sRoom1, sRoom3)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
iRoom1 = Room("Room1")
iRoom2 = Room("Room2")
iRoom3 = Room("Room3")
iRoom4 = Room("Room4")
iRoom5 = Room("Room5")
iRoom6 = Room("Room6")

# west, west, west, north, east.
iRoom1.setWest(iRoom2)
iRoom2.setWest(iRoom3)
iRoom3.setWest(iRoom4)
iRoom4.setNorth(iRoom5)
iRoom5.setEast(iRoom6)
INTERMEDIATE_MAZE = Maze(iRoom1, iRoom6)


if __name__=="__main__":
    
    play(INTERMEDIATE_MAZE)