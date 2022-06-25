import pygame
import sys
import random
from random import randint
from pygame.locals import *
pygame.init()

grey = (128,128,128)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


fps = 2
screen = pygame.display.set_mode((380,670))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    print()
    screen.fill(grey)