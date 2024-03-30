# Author: David Miller | djm545
# Date: 5/16/2023
# Purpose: The main script for a simple ping pong like game, read the readME.txt file

import pygame
from text import Text 
from ball import Ball
from paddle import Paddle
import random

pygame.init()
surface = pygame.display.set_mode((800, 600))
DREXEL_BLUE = (7, 41, 77)
DREXEL_GOLD = (255, 198, 0)
winNum = 50 # WIN CONDITION
maxNumOfBalls = 3 # MAX BALLS ALLOWED IN FIELD
pauseRemind = Text(f"SPACEBAR to Pause", 200, 10, DREXEL_BLUE)
gameGoal = Text(f"GOAL: Get {winNum} Points", 530, 10, DREXEL_BLUE)
pauseText = Text(f"PAUSED", 200, 200, DREXEL_GOLD, 100)
loseText = Text(f"YOU LOSE", 140, 250, (255, 100, 100), 100)
winText = Text(f"YOU WIN!!!", 125, 250, DREXEL_GOLD, 100)


fpsClock = pygame.time.Clock()
games = True

while games: # FOR MULTIPLE GAMES
    # Below initializes the basics for each game.
    myBalls = [Ball(400, 300, 20, DREXEL_GOLD)]
    myPaddle = Paddle(200, 15, DREXEL_GOLD) 
    myScoreBoard = Text("Score: 0", 10, 10, DREXEL_BLUE)
    numHits = 0
    maxBalls = maxNumOfBalls
    running = True # Starts the game
    pause = False
    
    while running: # THIS SPECIFIC GAME
        surface.fill(DREXEL_BLUE)
        pygame.draw.rect(surface, DREXEL_GOLD, (0, 0, 800, 40))
        myScoreBoard.draw(surface)
        gameGoal.draw(surface)
        pauseRemind.draw(surface)
        if not (len(myBalls) == 0 or numHits == winNum): # or myPaddle.isVisible(): WIP
            myPaddle.draw(surface)
            for ball in myBalls:
                if isinstance(ball, Ball):
                    if not ball.isLost(): # If ball is still in playable area
                        ball.draw(surface)
                        if ball.intersects(myPaddle):
                            ball.setYSpeed(ball.getYSpeed() * -1) # Reverse Y
                            if not ball.maxReached(): # If not max speed yet
                                ball.setYSpeed(ball.getYSpeed() * 1.15)
                                ball.setXSpeed(ball.getXSpeed() * 1.15)
                                ball.isMaxReached() # Check if current speed is max
                            if myPaddle.getWidth() >= 25 * (len(myBalls) + 2): # Width is at minimum 25 * (numBalls + 2)
                                myPaddle.setWidth(myPaddle.getWidth() - 5) # Decrease width
                            if (numHits + 1) % 10 == 0 and len(myBalls) < maxBalls: # If this makes a 10s mark on score board and if max balls aren't on field
                                myBalls.append(Ball(random.randint(200, 600), 300, 20, DREXEL_GOLD)) # New Ball at random x
                                myPaddle.setWidth(myPaddle.getWidth() + 20 + (5 * len(myBalls))) # Slightly increase Width
                            numHits += 1
                        if not pause:
                            ball.move() # Move balls beind scenes only when the game is unpaused
                        else:
                            pauseText.draw(surface)
                    elif ball.isLost(): # Ball is lost off of playable area
                        numHits -= 5 * (len(myBalls) - 1) # Subtract 5 times the number of balls minus one from score
                        myBalls.remove(ball) # Remove it from the list
                        myPaddle.setWidth(myPaddle.getWidth() - 30) # Decrease Width
                        maxBalls += .25 # Every four balls lost is one more needed to win
                    myScoreBoard.setMessage("Score: " + str(numHits))
        elif numHits == winNum: # WIN
            winText.draw(surface)
        else: # LOSE
            loseText.draw(surface)
            
        for event in pygame.event.get(): # pygame events
            if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                games = False
                running = False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                running = False # Starts a new Game
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                myPaddle.toggleVisible() # Stop drawing Paddle
                for ball in myBalls:
                    ball.toggleVisible() # Stop drawing Balls
                pause = False if pause else True # If paused: unpause, if unpaused: pause
        pygame.display.update()
        fpsClock.tick(30) # Approx. 30 Frames Per Second
exit() 
