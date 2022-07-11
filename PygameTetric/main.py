import random
import sys

import pygame
from pygame.locals import *

from pygame import sysfont
pygame.init()
screen = pygame.display.set_mode((800,600))
FPS = 60
FramePerSecond = pygame.time.Clock()
pygame.display.set_caption("Tetric")

green = (0,255,0)
red = (255,0,0)
onecell = pygame.image.load("onecell.png")

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSecond.tick(FPS)














