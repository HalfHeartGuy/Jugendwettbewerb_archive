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


fps = 2
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()








while True:
    relpositionlists = [[2, 3], [2, 4], [2, 5], [2, 6]]
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    screen.fill(grey)
    onepiece = tetrisclasses.Piece(screen,0,0,green,10,relpositionlists)
    onepiece.draw(screen)
