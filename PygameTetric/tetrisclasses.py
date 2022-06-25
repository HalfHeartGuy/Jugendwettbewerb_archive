import pygame
import sys
from pygame.locals import *
import random



class Piece(pygame.sprite.Sprite):
    def __init__(self,screen,startposX,startposY,color,width,relPositionList):
        self.screen = screen
        self.color = color
        self.width = width
        self.absolutPositionList = []

        #realtive pos sample: relpositionlists = [[2,3],[2,4],[2,5],[2,6]]

        for onepos in relPositionList:
            self.absolutPositionList.append([startposX + onepos[0] * width,startposY + onepos[1] * width])

    def draw(self,surface):
        for onepos in self.absolutPositionList:
            pygame.draw.rect(surface,self.color,(onepos[0],onepos[1],self.width,self.width))



