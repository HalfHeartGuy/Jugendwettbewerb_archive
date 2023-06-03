
import pygame

pygame.init()
from pygame import Surface

def drawCircle(screen:Surface):
    color_white = (255,255,255)
    color_grey = (128,128,128)
    screen.fill(color_grey)
    color_circle = (0,255,0)
    circle_center = (255,255)
    circle_radius = 50
    pygame.draw.circle(screen,color_circle,circle_center,circle_radius)


class Button():
    def __init__(self, main_screen:str,text: str, pos: tuple, font, bg="black", feedback=""):
        self.main_screen = main_screen
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.feedback = feedback

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def click(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.change_text(self.feedback, bg="red")

    def show(self):
        self.main_screen.blit(self.surface,(self.x,self.y))

    def createANewUserInMySQLTable(self):
        pass