

class playerClass:

    import pygame
    import random
    import os
    import math
    import sys

    plyrVelX = 0
    plyrVelY = 0
    plyrX = 400
    plyrY = 400
    facing = 0

    velReset = 0
    upPress = 0
    downPress = 0
    leftPress = 0
    rightPress = 0



    def playerKeypress(self):

        from window import windowClass
        from pygame import event

        import pygame



        event = pygame.event.poll()


        # UP

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.upPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            self.upPress = 0
            print("hello")

        # DOWN

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.downPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            self.downPress = 0
            print("hello")

        # LEFT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.leftPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.leftPress = 0
            print("hello")

        # RIGHT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rightPress = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.rightPress = 0
            print("hello")

        # STOP

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            self.velReset = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            self.velReset = 0

            print("hello")

    def playerVelCalc(self):

        # Facing
        if self.upPress == 1 and self.rightPress == 1:
            self.facing = 1

        elif self.rightPress == 1 and self.downPress == 1:
            self.facing = 3

        elif self.downPress == 1 and self.leftPress == 1:
            self.facing = 5

        elif self.leftPress == 1 and self.upPress == 1:
            self.facing = 7

        elif self.upPress == 1:
            self.facing = 0

        elif self.downPress == 1:
            self.facing = 4

        elif self.leftPress == 1:
            self.facing = 6

        elif self.rightPress == 1:
            self.facing = 2

        # Velocity
        if self.velReset == 1:
            self.plyrVelX = 0
            self.plyrVelY = 0

        if self.upPress == 1:
            self.plyrVelY -= 0.0005

        if self.downPress == 1:
            self.plyrVelY += 0.0005

        if self.leftPress == 1:
            self.plyrVelX -= 0.0005

        if self.rightPress == 1:
            self.plyrVelX += 0.0005

    def playerCalcPos(self):

        # Posision
        self.plyrX += self.plyrVelX
        self.plyrY += self.plyrVelY

    def playerDraw(self):

        from window import windowClass
        import pygame

        # Drawing player
        pygame.draw.rect(windowClass.screen, [0, 255, 0], [self.plyrX, self.plyrY, 11, 11])

        #Drawing gun thing
        if self.facing == 0:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + 5, self.plyrY + -10], 1)
            pygame.display.flip()
        elif self.facing == 1:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + 17.5, self.plyrY + -7.5], 1)
            pygame.display.flip()
        elif self.facing == 2:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + 20, self.plyrY + 5], 1)
            pygame.display.flip()
        elif self.facing == 3:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + 17.5, self.plyrY + 17.5], 1)
            pygame.display.flip()
        elif self.facing == 4:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + 5, self.plyrY + 20], 1)
            pygame.display.flip()
        elif self.facing == 5:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + -7.5, self.plyrY + 17.5], 1)
            pygame.display.flip()
        elif self.facing == 6:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + -10, self.plyrY + 5], 1)
            pygame.display.flip()
        elif self.facing == 7:
            pygame.draw.line(windowClass.screen, [0,200,0], [self.plyrX + 5, self.plyrY + 5],[self.plyrX + -7.5, self.plyrY + -7.5], 1)
            pygame.display.flip()
