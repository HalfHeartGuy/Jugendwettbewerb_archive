import pygame as pygame


class TetricPiece(pygame.sprite.Sprite):
    def __init__(self, screen,absoluteStartPosX, absoluteStartPosY, cellImage, cellWidth, startRelPosition):
        super().__init__()
        self.absoluteStartPosX = absoluteStartPosX
        self.absoluteStartPosY = absoluteStartPosY
        self.image = pygame.image.load(cellImage) ##"gameMaterial/player1.gif"
        self.curRotation = startRelPosition ## Beispiel [[2,0],[2,1],[2,2],[2,3]] steht für Tetric_I
        self.rotationList = [startRelPosition] ## Beispiel [[[2,0],[2,1],[2,2],[2,3]], zweite Rotation, dritte Rotation] steht für Tetric_I
        self.startRelPosition = startRelPosition
        self.absolutPositionList = []
        self.cellWidth = cellWidth
        self.screen = screen


        self.rect = self.image.get_rect()
        self.rect.center = (200,500)
        #self.rect.size = (1,1)

        for onepos in self.curRotation:

            self.absolutPositionList.append([self.absoluteStartPosX + onepos[0] * self.cellWidth, self.absoluteStartPosY + onepos[1] * self.cellWidth])
    def draw(self,surface):



        for onePos in self.curRotation:
            IMAGE = self.image.convert()
            rect = self.image.get_rect()
            rect.center = (onePos[0], onePos[1])
            rect.width = self.cellWidth
            rect.height = self.cellWidth
            green = (0,255,0)
            self.screen.blit(IMAGE, rect)

    def calcRotationList(self):
        print("nothing done, need specical coding in Subclass")

    def rotate(self):
        print("just go to next rotation")

class PieceI(TetricPiece):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("ich bin ein I")


class PieceL(TetricPiece):
    def __init__(self,absoluteStartPosX,absoluteStartPosY,cellImage,cellWidth,startRelPosition):
        TetricPiece.__init__(self,absoluteStartPosX,absoluteStartPosY,cellImage,cellWidth,startRelPosition)
        self.rotationCenter = self.startRelPosition[2]
        self.rotationList = [self.startRelPosition]
        self.calcRotationList()
        self.curRotationIndex = 0
        self.curRotation = self.rotationList[self.curRotationIndex]

    def draw(self):
        print("to left")
    def calcRotationList(self):
        rotationCenterX = self.rotationCenter[0]
        rotationCenterY = self.rotationCenter[1]

        rotation1 = [[rotationCenterX, rotationCenterY - 2],[rotationCenterX,rotationCenterY - 1],[rotationCenterX,rotationCenterY],[rotationCenterX + 1,rotationCenterY]]
        rotation2 = [[rotationCenterX, rotationCenterY + 1],[rotationCenterX,rotationCenterY] , [rotationCenterX + 1,rotationCenterY],[rotationCenterX + 2,rotationCenterY]]
        rotation3 = [[rotationCenterX - 1,rotationCenterY],[rotationCenterX,rotationCenterY],[rotationCenterX,rotationCenterY + 1],[rotationCenterX + 2,rotationCenterY]]
        rotation4 = [[rotationCenterX,rotationCenterY - 1],[rotationCenterX,rotationCenterY],[rotationCenterX - 1,rotationCenterY],[rotationCenterX - 2,rotationCenterY]]

        self.rotationList = [rotation1,rotation2,rotation3,rotation4]


    def rotate(self):
        self.curRotationIndex += 1
        if (self.curRotationIndex >= len(self.rotationList)):
            self.curRotationIndex = 0
        self.curRotation = self.rotationList[self.curRotationIndex]

    def dropDown(self):
        rotationCenterX = self.rotationCenter[0]
        rotationCenterY = self.rotationCenter[1]
        self.rotationCenter = [rotationCenterX,rotationCenterY + 1]
        self.calcRotationList()
        self.curRotation = self.rotationList[self.curRotationIndex]

    def moveLeft(self):
        rotationCenterX = self.rotationCenter[0]
        rotationCenterY = self.rotationCenter[1]
        self.rotationCenter = [rotationCenterX - 1,rotationCenterY]
        self.calcRotationList()
        self.curRotation = self.rotationList[self.curRotationIndex]

    def moveRight(self):
        rotationCenterX = self.rotationCenter[0]
        rotationCenterY = self.rotationCenter[1]
        self.rotationCenter = [rotationCenterX + 1,rotationCenterY]
        self.calcRotationList()
        self.curRotation = self.rotationList[self.curRotationIndex]

    def print(self):
        print("current Rotation List")
        print("" + str(self.curRotation))
        print("current rotationlist " + str(self.rotationList))



onePieceL = PieceL(0,0,"onecell.png",10,[[3,0],[3,1],[3,2],[4,2]])
onePieceL.print()
onePieceL.moveRight()
onePieceL.print()
onePieceL.moveLeft()
onePieceL.print()
curRotation = 4


