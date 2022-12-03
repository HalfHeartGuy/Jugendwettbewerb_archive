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

chess_board_start_x = 550
chess_board_start_y = 150
cell_width = 80






colorchange = 0

DISPLAYSURF = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption("My Chess v0.1")

DISPLAYSURF.fill(grey)
# Frames per second
FPS = pygame.time.Clock()
FPS.tick(30)



#Class für Chess_Sprite


class Tower(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



Chess.draw_chess_board(chess_board_start_x,chess_board_start_y,cell_width,DISPLAYSURF)
chess_sprite_white_tower = Tower(chess_board_start_x + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"Schach/image_tower.jpg")



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    chess_sprite_white_tower.draw(DISPLAYSURF)
    pygame.display.update()
