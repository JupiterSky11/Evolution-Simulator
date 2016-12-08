
from gameEngine import screen

import pygame
import random
import os
import math
import sys
import gameEngine

class playerClass:

    def playerFunc(self):
        velReset = 0
        upPress = 0
        downPress = 0
        leftPress = 0
        rightPress = 0

        plyrVelX = 0
        plyrVelY = 0
        plyrX = gameEngine.windowSizeX / 2
        plyrY = gameEngine.windowSizeY / 2
        facing = 0




        # UP

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            upPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            upPress = 0

        # DOWN

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            downPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            downPress = 0

        # LEFT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            leftPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            leftPress = 0

        # RIGHT

        if event.type == pygame.KEYDOWN and pygame.event.key == pygame.K_d:
            rightPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            rightPress = 0

        # STOP

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            velReset = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            velReset = 0

        # Facing
        if upPress == 1 and rightPress == 1:
            facing = 1

        elif rightPress == 1 and downPress == 1:
            facing = 3

        elif downPress == 1 and leftPress == 1:
            facing = 5

        elif leftPress == 1 and upPress == 1:
            facing = 7

        elif upPress == 1:
            facing = 0

        elif downPress == 1:
            facing = 4

        elif leftPress == 1:
            facing = 6

        elif rightPress == 1:
            facing = 2

        # Velocity
        if velReset == 1:
            plyrVelX = 0
            plyrVelY = 0

        if upPress == 1:
            plyrVelY -= 0.0005

        if downPress == 1:
            plyrVelY += 0.0005

        if leftPress == 1:
            plyrVelX -= 0.0005

        if rightPress == 1:
            plyrVelX += 0.0005

        # Posision
        plyrX += plyrVelX
        plyrY += plyrVelY

        #Drawing gun thing
        if facing == 0:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + 5, plyrY + -10], 1)

        elif facing == 1:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + 17.5, plyrY + -7.5], 1)

        elif facing == 2:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + 20, plyrY + 5], 1)

        elif facing == 3:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + 17.5, plyrY + 17.5], 1)

        elif facing == 4:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + 5, plyrY + 20], 1)

        elif facing == 5:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + -7.5, plyrY + 17.5], 1)

        elif facing == 6:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + -10, plyrY + 5], 1)

        elif facing == 7:
            pygame.draw.line(screen, [0,200,0], [plyrX + 5, plyrY + 5],[plyrX + -7.5, plyrY + -7.5], 1)


        # Drawing player
        pygame.draw.rect(screen, [0, 255, 0], [plyrX, plyrY, 11, 11])


        #Displaying the changes
        pygame.display.flip()
