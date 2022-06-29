import pygame
import sys
from pygame.locals import *
import random



class Piece(pygame.sprite.Sprite):
    def __init__(self, screen, startposX, startposY, imagename, width, relPositionList):
        self.screen = screen
        self.width = width
        self.absolutPositionList = []
        self.imageName = imagename
        self.rotatelist = [relPositionList]


        #realtive pos sample: relpositionlists = [[2,3],[2,4],[2,5],[2,6]]

        for onepos in relPositionList:
            self.absolutPositionList.append([startposX + onepos[0] * width,startposY + onepos[1] * width])



    def draw(self,surface):
        for onePos in self.absolutPositionList:
            IMAGE = pygame.image.load(self.imageName).convert()
            rect = IMAGE.get_rect()
            rect.center = (onePos[0], onePos[1])
            rect.width = self.width
            rect.height = self.width
            green = (0,255,0)

            self.screen.blit(IMAGE, rect)
    def calcRotationList(self,relPositionList):
        self.rotationlist = relPositionList
        self.rotationlistcalcrotation = []
        counter = 1
        while counter < len(self.rotationlist):
            if counter == 1:
                onecoordinateList = []
                for onecoordinate in self.rotationlist:
                    onecoordinateList.append(onecoordinate[0] - 1)
                    onecoordinateList.append(onecoordinate[1] + 1)



            if counter == 2:
                self.rotationlistcalcrotation.append(self.rotationlist[counter - 1])









    def rotate(self):
        pass

        #Berechnung vom restlichen möglichen Rotationen
   # def rotate(self):


    # Create a rect with the size of the image.




