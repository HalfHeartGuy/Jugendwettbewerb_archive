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
    relPositionListsL = [[[5,5],[5,6],[6,6],[7,6]]]





    pygame.display.update()
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    curRotate = curRotateClass.calcCurrentRotateI()

    clock.tick(fps)
    screen.fill(grey)









    onepiece = tetrisclasses.PieceI(screen, 0, 0, "onecell.png", 20, relpositionlistsI[0])
    relpositionlistsI.append(onepiece.calcRotationListI(relpositionlistsI))


    onepiece2Rotation = tetrisclasses.PieceI(screen,0,0,"onecell.png",20,relpositionlistsI[1])




    onePieceL = tetrisclasses.PieceL(screen,5,5,"onecell.png",20,relPositionListsL[0])
    relPositionListsL.append(onePieceL.calcRotationListL1(relPositionListsL))
    relPositionListsL.append(onePieceL.calcRotationListL2(relPositionListsL))
    relPositionListsL.append(onePieceL.calcRotationListL3(relPositionListsL))




    onePieceL2 = tetrisclasses.PieceL(screen,5,5,"onecell.png",20,relPositionListsL[1])
    onePieceL3 = tetrisclasses.PieceL(screen,5,5,"onecell.png",20,relPositionListsL[2])
   # onePieceL4 = tetrisclasses.PieceL(screen,5,5,"onecell.png",20,relPositionListsL[3])


    curRotateLClass = tetrisclasses.curRotateL()
    curRotateL = curRotateLClass.calcCurrentRotateL()
    if curRotateL == 0:
        onePieceL.draw(screen)

    if curRotateL == 1:
        onePieceL2.draw(screen)
    if curRotateL == 2:
        onePieceL3.draw(screen)
    #if curRotateL == 3:
     #   onePieceL4.draw(screen)







    if curRotate == 0:
        onepiece.draw(screen)
    if curRotate == 1:
        onepiece2Rotation.draw(screen)







