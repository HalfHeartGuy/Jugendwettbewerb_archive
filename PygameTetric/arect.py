import pygame
from pygame.locals import *
import sys

display = pygame.display.set_mode((400,500))
grey = (128,128,128)
display.fill(grey)

FramePerSecond = pygame.time.Clock()
FPS = 10



background = pygame.image.load("AnimatedStreet.png")

class Square(pygame.sprite.Sprite):
    def __init__(self,cellwidth,cellPositionX,cellPositionY):
        super().__init__()
        self.cellwidth = cellwidth
        self.image = pygame.image.load("onecell.png")
        self.cellPositionX = cellPositionX * cellwidth
        self.cellPositionY = cellPositionY * cellwidth
        self.rect = self.image.get_rect()
        self.rect.center = (self.cellPositionX,self.cellPositionY)






"""
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.cellPositionX -= self.cellwidth
            self.rect.move_ip(-self.cellwidth,0)
        if keys[K_RIGHT]:
            self.cellPositionX += self.cellwidth
            self.rect.move_ip(self.cellwidth,0)

   #     self.rect.center = (self.cellPositionX,self.cellPositionY)
"""
#Figure I

figureI = pygame.sprite.Group()

square = Square(20,5,5)
square2 = Square(20,6,5)
square3 = Square(20,7,5)
square4 = Square(20,8,5)



#print("square type " + str(type(square)))


#figureI.add(Square(20,100,100))
figureI.add(square)
figureI.add(square2)
figureI.add(square3)
figureI.add(square4)












#-----------------------------------------#





while True:
    square.move()
    square2.move()
    square3.move()
    square4.move()
    display.blit(background, (0,0))
    display.blit(square.image, square.rect)
    display.blit(square2.image, square2.rect)
    display.blit(square3.image, square3.rect)
    display.blit(square4.image, square4.rect)




    pygame.display.update()




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSecond.tick(FPS)



