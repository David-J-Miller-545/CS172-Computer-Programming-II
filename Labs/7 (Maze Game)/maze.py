#Mark Boady
#CS 172 - Maze Game
#Drexel University 2018

class Maze:
    #Inputs: Pointers to start room and exit room
    #Sets current to be start room
    def __init__(self, st = None, ex = None):
        pass
        #Room the player starts in
        self.__st = st
        #If the player finds this room they win
        self.__ex = ex
        #What room is the player currently in
        self.__curr = st

    #Return the room the player is in (current)
    def getCurrent(self):
        return self.__curr

    #The next four methods all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new room (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
        n = self.__curr.getNorth()
        if n == None:
            return False
        else:
            self.__curr = n
            return True
    
    def moveSouth(self):
        s = self.__curr.getSouth()
        if s == None:
            return False
        else:
            self.__curr = s
            return True
        
    def moveEast(self):
        e = self.__curr.getEast()
        if e == None:
            return False
        else:
            self.__curr = e
            return True
    
    def moveWest(self):
        w = self.__curr.getWest()
        if w == None:
            return False
        else:
            self.__curr = w
            return True

    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        return True if self.__curr == self.__ex else False

    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start room
    def reset(self):
        self.__curr = self.__st
