#Simple Maze Class
#Mark Boady
#Drexel University
#CS 172

class Room:
    #Constructor sets the description
    #And all four doors should be initially set to None
    def __init__(self, descr):
        # TODO
        self.__descr = descr
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        
    #Accessors
    #Return the correct values
    def __str__(self):
        # TODO: 
        return self.__descr
    
    def getNorth(self):
        return self.__north
    
    def getSouth(self):
        return self.__south
    
    def getEast(self):
        return self.__east
    
    def getWest(self):
        return self.__west
        
    #Mutators
    #Update the values
    def setDescription(self, d):
        self.__descr = d
    
    def setNorth(self, n):
        self.__north = n
    
    def setSouth(self, s):
        self.__south = s
    
    def setEast(self, e):
        self.__east = e
    
    def setWest(self, w):
        self.__west = w
    