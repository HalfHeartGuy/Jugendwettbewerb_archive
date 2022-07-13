import time

import pygame
import sys
from pygame.locals import *
import random



class PieceI(pygame.sprite.Sprite):
    def __init__(self, screen, startposX, startposY, imagename, width, relPositionList):
        self.screen = screen
        self.width = width
        self.absolutPositionList = []
        self.imageName = imagename
        self.rotateList = [relPositionList]
      #  self.currentRotate = 0


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

    def calcRotationListI(self,relPositionList):
        counter = 1
        self.rotationlist = []
        while counter < 5:
            if counter == 1:
                twocoordinates = []

                twocoordinates.append(relPositionList[0][counter - 1][0] - 1)
                twocoordinates.append(relPositionList[0][counter - 1][1] + 1)
                self.rotationlist.append(twocoordinates)
                counter += 1
            if counter == 2:
                twocoordinates = []

                twocoordinates.append(relPositionList[0][counter - 1][0])
                twocoordinates.append(relPositionList[0][counter - 1][1])
                self.rotationlist.append(twocoordinates)
                counter += 1

            if counter == 3:
                twocoordinates = []

                twocoordinates.append(relPositionList[0][counter - 1][0] + 1)
                twocoordinates.append(relPositionList[0][counter - 1][1] - 1)
                self.rotationlist.append(twocoordinates)
                counter += 1

            if counter == 4:
                twocoordinates = []

                twocoordinates.append(relPositionList[0][counter - 1][0] + 2)
                twocoordinates.append(relPositionList[0][counter - 1][1] - 2)
                self.rotationlist.append(twocoordinates)
                counter += 1
        return self.rotationlist



class CurRotate(pygame.sprite.Sprite):
    def __init__(self):
        self.currentRotate = 0
    def calcCurrentRotateI(self):
        keysI = pygame.key.get_pressed()
        if keysI[K_UP]:
            self.currentRotate = 1
        if keysI[K_DOWN]:
            self.currentRotate = 0
        return self.currentRotate

class PieceL(pygame.sprite.Sprite):
    def __init__(self, screen, startposX, startposY, imagename, width, relPositionList):
        self.screen = screen
        self.width = width
        self.absolutPositionList = []
        self.imageName = imagename
        self.rotateList = [relPositionList]
        self.currentRotate = 0

        # realtive pos sample: relpositionlists = [[2,3],[2,4],[2,5],[2,6]]

        for onepos in relPositionList:
            self.absolutPositionList.append([startposX + onepos[0] * width, startposY + onepos[1] * width])

    def draw(self, surface):


        for onePos in self.absolutPositionList:
            IMAGE = pygame.image.load(self.imageName).convert()
            rect = IMAGE.get_rect()
            rect.center = (onePos[0], onePos[1])
            rect.width = self.width
            rect.height = self.width
            green = (0, 255, 0)
            self.screen.blit(IMAGE, rect)

    def calcRotationListL1(self, relPositionList):
        counter = 1
        self.relPositionList = relPositionList
        self.rotationlist2 = []
        while counter < 5:
            if counter == 1:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] * 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] + 2)
                self.rotationlist2.append(twocoordinates)
                counter += 1
            if counter == 2:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] + 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] - 1)
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 3:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0])
                twocoordinates.append(self.relPositionList[0][counter - 1][1])
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 4:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] - 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] + 1)
                self.rotationlist2.append(twocoordinates)
                counter += 1


        return self.rotationlist2
    def calcRotationListL2(self,relPositionList):
        counter = 1
        self.relPositionList = relPositionList
        self.rotationlist2 = []
        while counter < 5:
            if counter == 1:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] + 2)
                twocoordinates.append(self.relPositionList[0][counter - 1][1])
                self.rotationlist2.append(twocoordinates)
                counter += 1
            if counter == 2:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] + 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] + 1)
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 3:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0])
                twocoordinates.append(self.relPositionList[0][counter - 1][1])
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 4:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] - 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] - 1)
                self.rotationlist2.append(twocoordinates)
                counter += 1


        return self.rotationlist2
    def calcRotationListL3(self,relPositionList):
        counter = 1
        self.relPositionList = relPositionList
        self.rotationlist2 = []
        while counter < 5:
            if counter == 1:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] + 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] + 3)
                self.rotationlist2.append(twocoordinates)
                counter += 1
            if counter == 2:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] + 1)
                twocoordinates.append(self.relPositionList[0][counter - 1][1] + 1)
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 3:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0])
                twocoordinates.append(self.relPositionList[0][counter - 1][1])
                self.rotationlist2.append(twocoordinates)
                counter += 1

            if counter == 4:
                twocoordinates = []

                twocoordinates.append(self.relPositionList[0][counter - 1][0] - 2)
                twocoordinates.append(self.relPositionList[0][counter - 1][1])
                self.rotationlist2.append(twocoordinates)
                counter += 1







class curRotateL(pygame.sprite.Sprite):
    def __init__(self):
        self.currentRotate = 0
    def calcCurrentRotateL(self):
        keysL = pygame.key.get_pressed()
        if keysL[K_1]:
            self.currentRotate = 0
        if keysL[K_2]:
            self.currentRotate = 1
        if keysL[K_3]:
            self.currentRotate = 2
        if keysL[K_4]:
            self.currentRotate = 3

        return self.currentRotate






"""
    def rotate(self):
        currentRotate = 








        #Berechnung vom restlichen möglichen Rotationen
   # def rotate(self):


    # Create a rect with the size of the image.

"""


