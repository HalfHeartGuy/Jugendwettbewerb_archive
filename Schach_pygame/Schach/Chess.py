import pygame
from pygame.locals import *
import sys
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (255, 0, 0)

def draw_chess_board(start_x,start_y,cellwidth,DISPLAYSURF):




    color = black
    for y in range(9,1,-1):
        if color == white:
            color = black
        else:
            color = white
        for x in range(6,14):
            if color == white:
                color = black
            else:
                color = white
            pygame.draw.rect(DISPLAYSURF,color,[x * cellwidth,y * cellwidth,cellwidth,cellwidth])
