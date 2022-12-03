import pygame
from pygame.locals import *
import sys
from Schach import Chess
from Chess import *
import time
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (255, 0, 0)
colorchange = 0

DISPLAYSURF = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption("My Chess v0.1")

DISPLAYSURF.fill(grey)
# Frames per second
FPS = pygame.time.Clock()
FPS.tick(30)


Chess.draw_chess_board(100,100,30,DISPLAYSURF)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
