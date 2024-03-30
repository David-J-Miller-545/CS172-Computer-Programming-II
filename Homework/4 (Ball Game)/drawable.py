# Author: David Miller | djm545
# Date: 5/16/2023
# Purpose: Abstaract Base Class for every drawable object

from abc import ABC
import pygame

class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__visible = True
        self.__x = x
        self.__y = y

    def draw(self, surface):
        pass

    def get_rect(self):
        pass

    def getLoc(self):
        return (self.__x, self.__y)
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
        
    def isVisible(self):
        return self.__visible

    def toggleVisible(self):
        if self.__visible:
            self.__visible = False
        else:
            self.__visible = True
        
    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
            return True
        return False
