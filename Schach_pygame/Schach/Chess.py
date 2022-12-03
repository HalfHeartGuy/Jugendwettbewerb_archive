import pygame
from pygame.locals import *
import sys
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (255, 0, 0)

def draw_chess_board(start_x, start_y, cellwidth, screen):

    cell_color = white



    for row in range(0,8):

        # eine Reihe zeichnen
        for i in range(0,8):
            cell_i_x = start_x + i * cellwidth
            cell_i_y = start_y + row * cellwidth

            pygame.draw.rect(screen,cell_color,[cell_i_x,cell_i_y,cellwidth,cellwidth])
            cell_color = switchCellColor(cell_color)
        cell_color = switchCellColor(cell_color)



def switchCellColor(current_cell_color):
    if current_cell_color == black:
        return white
    elif current_cell_color == white:
        return black







