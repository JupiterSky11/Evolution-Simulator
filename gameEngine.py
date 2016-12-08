


#Hello
import pygame
import random
import os
import math
import sys
import feeder

windowRunning = 1
windowSizeX = 1280
windowSizeY = 800

BLACK = 0,0,0


clock = 100000

while clock >= 0:
    clock -= 1

player = feeder.playerClass()

screen = pygame.display.set_mode([windowSizeX, windowSizeY])
pygame.display.set_caption("Movable Square")


while windowRunning == 1:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        windowRunning = 0


    #Refreshing the screen
    screen.fill(BLACK)

    player.playerFunc()

    #Displaying the changes
    pygame.display.flip()

