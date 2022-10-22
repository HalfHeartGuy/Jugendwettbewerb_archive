import pygame as pygame


class TetricPiece(pygame.sprite.Sprite):
    def __init__(self, screen,absoluteStartPosX, absoluteStartPosY, cellImage, cellWidth, startRelPosition):
        super().__init__()
        self.screen = screen
        self.absoluteStartPosX = absoluteStartPosX
        self.absoluteStartPosY = absoluteStartPosY
        self.cellWidth = cellWidth
        self.absolutPositionList = []
        self.image = pygame.image.load(cellImage) ##"gameMaterial/player1.gif"
        self.curRotation = startRelPosition ## Beispiel [[2,0],[2,1],[2,2],[2,3]] steht für Tetric_I
        self.rotationList = [startRelPosition] ## Beispiel [[[2,0],[2,1],[2,2],[2,3]], zweite Rotation, dritte Rotation] steht für Tetric_I


        #self.rect.size = (1,1)
        for onePos in startRelPosition:
            self.absolutPositionList.append([absoluteStartPosX + onePos[0] * cellWidth,absoluteStartPosY + onePos[1] * cellWidth])


    def draw(self,screen):

        for onePos in self.curRotation:
            IMAGE = self.image.convert()
            rect = IMAGE.get_rect()
            rect.center = (onePos[0], onePos[1])
            rect.width = self.cellWidth
            rect.height = self.cellWidth
            green = (0,255,0)
            self.screen.blit(IMAGE, rect)
    def calcRotationList(self,possibleRotations,relPositionList):
        # voerst nur für L
        self.relPositionList = relPositionList
        counterForForLoop = 1
        self.relPositionListExtra = []












    def rotate(self):
        curRotationIndex = self.rotationList.index(self.curRotation + 1)
        if curRotationIndex + 1 >= len(self.rotationList):
            self.curRotation = self.rotationList[0]
        else:
            self.curRotation = self.rotationList[curRotationIndex + 1]


class PieceI(TetricPiece):
    def __init__(self):
        super().__init__()


    def draw(self):
        print("ich bin ein I")


class PieceL(TetricPiece):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("to left")
    def calcRotationList(self):
        super().__init__()

        rotation1 = [[]]


class PieceT(TetricPiece):
    def __init__(self):
        super().__init__()


    def draw(self):
        print("to left")