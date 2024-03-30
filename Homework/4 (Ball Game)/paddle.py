# Author: David Miller | djm545
# Date: 5/16/2023
# Purpose: This is the Paddle class that inherits from Drawable and contains the basics of the paddle

from drawable import Drawable
import pygame

class Paddle(Drawable):
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height
        self.__xSpeed = 10

    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width
    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.rect(surface, self.__color, self.get_rect())

    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        
        x = pygame.mouse.get_pos()[0]
        
        return pygame.Rect(x - self.__width/2,
                           screenHeight - 40 - (self.__height),
                           self.__width, self.__height)
                           

