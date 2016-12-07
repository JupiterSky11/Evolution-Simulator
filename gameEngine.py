#Hello
import pygame
import random
import os
import math
import sys

windowRunning = 1
windowSizeX = 1200
windowSizeY = 800

velReset = 0
upPress = 0
downPress = 0
leftPress = 0
rightPress = 0

plyrVelX = 0
plyrVelY = 0
plyrX = 30
plyrY = 30

facing = 0

BLACK = 0,0,0



screen = pygame.display.set_mode([windowSizeX, windowSizeY])
pygame.display.set_caption("Movable Square")


while windowRunning == 1:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        windowRunning = 0


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


    #RIGHT

    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        rightPress = 1
    if event.type == pygame.KEYUP and event.key == pygame.K_d:
        rightPress = 0

    #STOP

    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        velReset = 1
    if event.type == pygame.KEYUP and event.key == pygame.K_r:
        velReset = 0



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



    plyrX += plyrVelX
    plyrY += plyrVelY

    screen.fill(BLACK)

    pygame.draw.rect(screen, [0,255,0], [plyrX, plyrY, 10, 10])

    if facing == 0:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 5],[plyrX + 4, plyrY + -10], 2)

    if facing == 1:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 16, plyrY + -7], 2)

    if facing == 2:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)

    if facing == 3:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)

    if facing == 4:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)

    if facing == 5:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)

    if facing == 6:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)

    if facing == 7:
        pygame.draw.line(screen, [0,200,0], [plyrX + 4, plyrY + 4],[plyrX + 20, plyrY + 4], 2)


    pygame.display.flip()

    print(plyrY,plyrX)


