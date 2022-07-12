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
        self.cellwidth = cellwidth
        self.image = pygame.image.load("onecell.png")
        self.cellPositionX = cellPositionX
        self.cellPositionY = cellPositionY
        self.rect = self.image.get_rect()
        self.rect.center = (cellPositionX,cellPositionY)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.cellPositionX -= self.cellwidth
            self.rect.move_ip(-self.cellwidth,0)
        if keys[K_RIGHT]:
            self.cellPositionX += self.cellwidth
            self.rect.move_ip(self.cellwidth,0)

   #     self.rect.center = (self.cellPositionX,self.cellPositionY)





square = Square(20,100,100)


while True:
    square.move()
    display.blit(background, (0,0))
    display.blit(square.image, square.rect)



    pygame.display.update()




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSecond.tick(FPS)



