import pygame
import os
import time


winRun = 1
winWidth = 1000
winHeight = 700
gameName = "Make Games Great Again"



pygame.init()


winWidth, winHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
winWidth = int(winWidth - winWidth / 4)
winHeight = int(winHeight - winHeight / 4)
if winWidth > 1600:
    winHeight = winHeight / (winWidth / 1600)
    width = 1600
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 125)


screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption(gameName)


while winRun == 1 :
    pygame.display.update()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        winRun = 0
