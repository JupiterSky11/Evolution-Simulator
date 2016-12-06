#! /usr/bin/env python
from pygame import event
import pygame
import random
import evoSimMain




class player1:
    """Player Class"""
    def player(self):
        playerX = 300
        playerY = 300
        playerVX = 0
        playerVY = 0
        playerBaseSize = 10

        playerX += playerVX
        playerY += playerVY

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            playerVY -= float(0.01)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            playerVY -= float(-0.01)

        pygame.draw.rect(evoSimMain.screen, [0, 255, 0], [playerX, playerY, playerBaseSize, playerBaseSize])
