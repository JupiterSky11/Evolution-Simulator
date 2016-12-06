#! /usr/bin/env python
import pygame
import pygame.key
import random
import creatureFeeder1

player1 = creatureFeeder1.playerFunc()

windowRunning = 1
windowX = 600
windowY = 1020
background = 0,0,0

stars = 500
starX = 10
starY = 10
starSize = 0
starSizeMin = 5
starSizeMax = 8
starBightness = 0
starBightnessMin = 150
starBightnessMax = 255

screen = pygame.display.set_mode((1020, 600))
pygame.display.set_caption("Evolution Simulator")



while windowRunning == 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        windowRunning = 0

    screen.fill(background)

#    while stars > 0:
#        starX = random.randint(0, 1020)
#        starY = random.randint(0, 600)
#        starSize = random.randint(starSizeMin, starSizeMax)
#        starBightness = random.randint(starBightnessMin, starBightnessMax)

#        pygame.draw.rect(screen, [starBightness, starBightness, starBightness], [starX, starY, starSize, starSize], 0)
#        stars = stars - 1

#    drawPlyr(100,100)
#    plyrVel()

    player1 = creatureFeeder1.player

    player1()

    pygame.display.flip()
