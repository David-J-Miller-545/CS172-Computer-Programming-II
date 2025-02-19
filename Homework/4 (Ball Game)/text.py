# Author: David Miller | djm545
# Date: 5/16/2023
# Purpose: Text inherits from Drawable and just contains basics for drawing a message.

from drawable import Drawable
import pygame

class Text(Drawable):

    def __init__(self, message="Pygame", x=0, y=0, color=(0,0,0), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)

    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLoc())

    def get_rect(self):
        return self.__surface.get_rect()

    def setMessage(self, message):
        self.__message = message 
