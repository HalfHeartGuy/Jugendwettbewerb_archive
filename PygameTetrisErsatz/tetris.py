import time

import pygame
import sys
import random
from random import randint
from pygame.locals import *
import tetrisclasses
pygame.init()

grey = (128,128,128)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


fps = 60
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


curRotateClass = tetrisclasses.CurRotate()


while True:
    relpositionlistsI = [[[2, 2], [2, 3], [2, 4], [2, 5]]]





    pygame.display.update()
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    curRotate = curRotateClass.calcCurrentRotate()

    clock.tick(fps)
    screen.fill(grey)









    onepiece = tetrisclasses.Piece(screen, 0, 0, "onecell.png", 20, relpositionlistsI[0])
    relpositionlistsI.append(onepiece.calcRotationListI(relpositionlistsI))


    onepiece2Rotation = tetrisclasses.Piece(screen,0,0,"onecell.png",20,relpositionlistsI[1])



    if curRotate == 0:
        onepiece.draw(screen)
    if curRotate == 1:
        onepiece2Rotation.draw(screen)






