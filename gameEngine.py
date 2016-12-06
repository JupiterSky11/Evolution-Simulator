#Hello
import pygame
import random
import os
import math
import sys

windowRunning = 1

upPress = 0
downPress = 0
leftPress = 0
rightPress = 0

plyrVelX = 0
plryVelY = 0
plryX = 30
plyrY = 30

BLACK = 0,0,0



pygame.display.set_caption("Movable Square")
screen = pygame.display.set_mode([1020, 600])

while windowRunning == 1:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        windowRunning = 0


    # UP

    if pygame.event == pygame.KEYDOWN and pygame.event.key == pygame.K_w:
        upPress = 1
    if pygame.event == pygame.KEYUP and pygame.event.key == pygame.K_w:
        upPress = 0


    # DOWN

    if pygame.event == pygame.KEYDOWN and pygame.event.key == pygame.K_s:
        downPress = 1
    if pygame.event == pygame.KEYUP and pygame.event.key == pygame.K_s:
        downPress = 0


    # LEFT

    if pygame.event == pygame.KEYDOWN and pygame.event.key == pygame.K_a:
        leftPress = 1
    if pygame.event == pygame.KEYUP and pygame.event.key == pygame.K_a:
        leftPress = 0


    #RIGHT

    if pygame.event == pygame.KEYDOWN and pygame.event.key == pygame.K_d:
        rightPress = 1
    if pygame.event == pygame.KEYUP and pygame.event.key == pygame.K_d:
        rightPress = 0



    if upPress == 1:
        plyrVelX += 1

    if downPress == 1:
        plyrVelX -= 0.01

    if leftPress == 1:
        plryVelY -= 0.01

    if rightPress == 1:
        plryVelY += 0.01



    plryX += plyrVelX
    plyrY += plryVelY

    screen.fill(BLACK)

    pygame.draw.rect(screen, [0,255,0], [plryX, plyrY, 10, 10])

    pygame.display.flip()


