# Author: David Miller | djm545
# Date: 5/16/2023
# Purpose: Ball class that inherits from Drawable and contains the basics of the ball

from drawable import Drawable
import pygame

class Ball(Drawable):
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 5
        self.__ySpeed = 5
        self.__lost = False
        self.__maxSpeed = False

    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
    
    def getXSpeed(self):
        return self.__xSpeed
    
    def setXSpeed(self, speed):
        self.__xSpeed = speed
    
    def getYSpeed(self):
        return self.__ySpeed
        
    def setYSpeed(self, speed):
        self.__ySpeed = speed
    
    def maxReached(self):
        return self.__maxSpeed
    
    def isMaxReached(self):
        self.__maxSpeed = True if self.__xSpeed >= 10 else False
        
    def isLost(self):
        return self.__lost
    
    def move(self):
        # Increase __x and __y by some amount
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed 
        self.setX(newX)
        self.setY(newY)
        
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1 

        if newY - 40 <= self.__radius:
            self.__ySpeed *= -1
        
        # IF BALL TOUCHES BOTTOM GAME OVER
        if newY + self.__radius >= height - 40 and not self.__lost:
            self.__ySpeed = 0
            self.__xSpeed = 0
            self.__lost = True
            
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius) 
