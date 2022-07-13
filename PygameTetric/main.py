import random
import sys

import pygame
from pygame.locals import *
import Tetrisvererbung2
from pygame import sysfont
pygame.init()
screen = pygame.display.set_mode((800,600))
FPS = 60
FramePerSecond = pygame.time.Clock()
pygame.display.set_caption("Tetric")

green = (0,255,0)
red = (255,0,0)
onecell = pygame.image.load("onecell.png")

onePieceL = Tetrisvererbung2.PieceL(0, 0, onecell, 10, [[3, 0], [3, 1], [3, 2], [4, 2]])

while True:

    onePieceL.draw(screen)
    onePieceL.moveRight()
    onePieceL.draw(screen)
    onePieceL.moveLeft()
    onePieceL.draw(screen)
    curRotation = 4





    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSecond.tick(FPS)














