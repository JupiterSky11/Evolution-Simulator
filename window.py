import pygame
import random
import os
import math
import sys

windowRunning = 1
windowSizeX = 1280
windowSizeY = 800



class windowClass:
    screen = pygame.display.set_mode([windowSizeX, windowSizeY])
    pygame.display.set_caption("Movable Square")

