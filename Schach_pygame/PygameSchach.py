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


class Figure_Chess_Visulisation(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = pygame.image.load(image)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



Chess.draw_chess_board(chess_board_start_x,chess_board_start_y,cell_width,DISPLAYSURF)
chess_sprite_white_tower = Figure_Chess_Visulisation(chess_board_start_x + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_tower.png")
chess_sprite_white_tower2 = Figure_Chess_Visulisation(chess_board_start_x + 7 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_tower.png")
chess_sprite_white_knight1 = Figure_Chess_Visulisation(chess_board_start_x + 6 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_knight.png")
chess_sprite_white_knight2 = Figure_Chess_Visulisation(chess_board_start_x + 1 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_knight.png")
chess_sprite_white_bishop1 = Figure_Chess_Visulisation(chess_board_start_x + 2 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_bishop.png")
chess_sprite_white_bishop2 = Figure_Chess_Visulisation(chess_board_start_x + 5 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_bishop.png")
chess_sprite_white_king = Figure_Chess_Visulisation(chess_board_start_x + 3 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_king.png")
chess_sprite_white_queen = Figure_Chess_Visulisation(chess_board_start_x + 4 * cell_width + 1/2 * cell_width,chess_board_start_y + 7 * cell_width + 1/2 * cell_width,"images/image_queen.png")
chess_sprite_white_pawns = []
chess_sprite_black_pawns = []
for i in range(0,8):
    chess_sprite_white_pawns.append(Figure_Chess_Visulisation(chess_board_start_x + i * cell_width + 1/2 * cell_width,chess_board_start_y + 6 * cell_width + 1/2 * cell_width,"images/image_pawn.png"))
for i in range(0,8):
    chess_sprite_black_pawns.append(Figure_Chess_Visulisation(chess_board_start_x + i * cell_width + 1/2 * cell_width,chess_board_start_y + 1 * cell_width + 1/2 * cell_width,"images/image_pawn_black.png"))
chess_sprite_black_king = Figure_Chess_Visulisation(chess_board_start_x + 3 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_king.png")
chess_sprite_black_queen = Figure_Chess_Visulisation(chess_board_start_x + 4 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_queen.png")
chess_sprite_black_bishop1 = Figure_Chess_Visulisation(chess_board_start_x + 2 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_bishop.png")
chess_sprite_black_bishop2 = Figure_Chess_Visulisation(chess_board_start_x + 5 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_bishop.png")
chess_sprite_black_knight1 = Figure_Chess_Visulisation(chess_board_start_x + 1 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_knight.png")
chess_sprite_black_knight2 = Figure_Chess_Visulisation(chess_board_start_x + 6 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/image_black_knight.png")
chess_sprite_black_tower1 = Figure_Chess_Visulisation(chess_board_start_x  + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/black_image_tower.png")
chess_sprite_black_tower2 = Figure_Chess_Visulisation(chess_board_start_x + 7 * cell_width + 1/2 * cell_width,chess_board_start_y + 1/2 * cell_width,"images/black_image_tower.png")



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    chess_sprite_white_tower.draw(DISPLAYSURF)
    chess_sprite_white_tower2.draw(DISPLAYSURF)
    chess_sprite_white_knight1.draw(DISPLAYSURF)
    chess_sprite_white_knight2.draw(DISPLAYSURF)
    chess_sprite_white_bishop1.draw(DISPLAYSURF)
    chess_sprite_white_bishop2.draw(DISPLAYSURF)
    chess_sprite_white_king.draw(DISPLAYSURF)
    chess_sprite_white_queen.draw(DISPLAYSURF)
    chess_sprite_black_king.draw(DISPLAYSURF)
    chess_sprite_black_queen.draw(DISPLAYSURF)
    chess_sprite_black_bishop1.draw(DISPLAYSURF)
    chess_sprite_black_bishop2.draw(DISPLAYSURF)
    chess_sprite_black_knight1.draw(DISPLAYSURF)
    chess_sprite_black_knight2.draw(DISPLAYSURF)
    chess_sprite_black_tower1.draw(DISPLAYSURF)
    chess_sprite_black_tower2.draw(DISPLAYSURF)




    for i in chess_sprite_white_pawns:
        i.draw(DISPLAYSURF)
    for i in chess_sprite_black_pawns:
        i.draw(DISPLAYSURF)
    pygame.display.update()
