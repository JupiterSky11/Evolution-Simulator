#! /usr/bin/env python
from pygame import event
import pygame
import random
import evoSimMain




class playerClass:
    """Player Class"""

    playerX = 300
    playerY = 300
    playerVX = 0
    playerVY = 0
    playerBaseSize = 10


    def playerFunc(self):

        playerClass.playerX += playerClass.playerVX
        playerClass.playerY += playerClass.playerVY

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            playerClass.playerVY -= float(0.01)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            playerClass.playerVY -= float(-0.01)

        pygame.draw.rect(evoSimMain.screen, [0, 255, 0], [playerClass.playerX, playerClass.playerY, playerClass.playerBaseSize, playerClass.playerBaseSize])
