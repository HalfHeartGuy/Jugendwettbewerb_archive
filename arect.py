import pygame
from pygame.locals import *
import sys

display = pygame.display.set_mode((500,500))
grey = (128,128,128)
display.fill(grey)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


