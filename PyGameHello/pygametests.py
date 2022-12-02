import pygame
import sys
from pygame.locals import *

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
pygame.draw.rect(DISPLAYSURF,white,[25,40,25,25])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()