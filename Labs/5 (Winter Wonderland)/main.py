# Author: David Miller | djm545
# Date: 5/3/2023
# Purpose: To simulate a winter wonderland with pygame

import pygame
from Drawable import Drawable, Rectangle, Snowflake
import random


surfWidth = 1280
surfHeight = 720
pygame.init()
pygame.display.set_caption("Winter Wonderland")
surface = pygame.display.set_mode( [surfWidth, surfHeight] )
sky = Rectangle(surfWidth, surfHeight*5/8, (135, 206, 235))
ground = Rectangle(surfWidth, surfHeight*3/8, (124, 252, 60), 0, surfHeight*5/8)
fall = True
snowflakes = []


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            # False if True, True if False
            fall = False if fall else True

    sky.draw(surface)
    ground.draw(surface)
    
            
    if fall:
        snowflakes.append(Snowflake(random.randint(0, surfWidth))) # New Snowflake
        for s in snowflakes:
            if isinstance(s, Snowflake): # Always True
                loc = s.getLoc()
                # ---Extra Credit---
                gbound = (random.randint(int(surfHeight*5/8), 10*surfHeight)) # 10 * surHeight so that flakes can land at the bottom or below the screen       
                if not s.getOnGround():
                    # If it is somewhere on the ground rect it is on the ground, else keep falling
                    s.flipOnGround() if loc[1] > gbound else s.setLoc((loc[0], loc[1] + 1))
                # ------------------
                s.draw(surface)
    else: # Freeze Frame
        for s in snowflakes:
            # Draw if a snowflake, else do nothing (print nothing)
            s.draw(surface) if isinstance(s, Snowflake) else print("", end = "") # Always True

    pygame.display.update()
