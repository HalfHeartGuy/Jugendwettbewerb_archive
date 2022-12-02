import pygame
from pygame.locals import *
import sys
import time

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (255, 0, 0)
colorchange = 0

DISPLAYSURF = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption("Chess")

DISPLAYSURF.fill(red)

# Frames per second
FPS = pygame.time.Clock()
FPS.tick(30)
width = 25
height = 25

def draw_chess_board():
    size = 100
    color = black
    for y in range(9,1,-1):
        if color == white:
            color = black
        else:
            color = white
        for x in range(5,13):
            if color == white:
                color = black
            else:
                color = white
            pygame.draw.rect(DISPLAYSURF,color,[x * size,y * size,size,size ])








draw_chess_board()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
