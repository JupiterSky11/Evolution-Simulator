clock = 100000
while clock >= 0:
    clock -= 1

#Hello
import pygame
import random
import os
import math
import sys
import feeder

import window
from window import windowRunning
from window import windowSizeX
from window import windowSizeY
from window import windowClass

clock = pygame.time.Clock()

BLACK = 0,0,0




player = feeder.playerClass()




while windowRunning == 1:



    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        windowRunning = 0


    #Refreshing the screen
    windowClass.screen.fill(BLACK)

    player.playerKeypress()
    player.playerVelCalc()
    player.playerDraw()

    #Displaying the changes
    pygame.display.flip()

