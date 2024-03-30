# Author: David Miller | djm545
# Date: 5/3/2023
# Purpose: Drawable classes/shapes

import pygame
from abc import ABC, abstractmethod

class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
        
    @abstractmethod
    def draw(self, surface):
        pass

class Rectangle(Drawable):
    def __init__(self, width, height, color = (0, 0, 0), x = 0, y = 0):
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        self.__height = height
        
    def draw(self, surface):
        loc = self.getLoc()
        x = loc[0]
        y = loc[1]
        
        self.setLoc( (x,y) )
        pygame.draw.rect(surface,self.__color,(loc[0],loc[1],self.__width,self.__height))


class Snowflake(Drawable):
    def __init__(self, x = 0):
        super().__init__(x)
        self.__color = (255, 255, 255)
        self.__onGround = False
        
    def getOnGround(self):
        return self.__onGround
    
    def flipOnGround(self):
        self.__onGround = False if self.__onGround else True
        
    def draw(self, surface):
        loc = self.getLoc()
        x = loc[0]
        y = loc[1]
        self.setLoc( (x,y) )
        
        pygame.draw.line(surface, self.__color, (x-5,y), (x+5, y))
        pygame.draw.line(surface, self.__color, (x,y-5), (x, y+5))
        pygame.draw.line(surface, self.__color, (x-5,y-5), (x+5, y+5))
        pygame.draw.line(surface, self.__color, (x-5,y+5), (x+5, y-5))
