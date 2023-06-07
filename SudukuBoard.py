import mysql.connector
import math
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "sudoku"
)
mycursor = mydb.cursor()
import pygame
from pygame import Surface
pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)



def drawCircle(screen: Surface):
    color_grey = (200, 200, 200)
    screen.fill(color_grey)
    color_circle = (0, 255, 0)
    circle_center = (250, 250)
    circle_radius = 80
    pygame.draw.circle(screen, color_circle, circle_center, circle_radius)


class Button():
    def __init__(self, text, pos, font, bg="black", feedback = ""):
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.feedback = feedback
        self.change_text(text, bg)  # Aufruf der change_text-Methode im Konstruktor

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
                    self.createANewUserInMySQLTable("Max",random.randint(6,99),"Max.Mustermann@gmail.com",str(random.randint(100,99999)) + "!",random.randint(11111111,99999999),str(random.randint(100,999)) + "." + str(random.randint(10,99)) + str(random.randint(100,999)) + "." + str(random.randint(10,99)),"DE")

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def createANewUserInMySQLTable(self,name,age,email,password,phone_number,IP,country):

        sql = "INSERT INTO user (Name, age,email, password, phone_number, IP, Land) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name,age,email,password,phone_number,IP,country)
        mycursor.execute(sql,values)

        mydb.commit()

        print(mycursor.rowcount)








