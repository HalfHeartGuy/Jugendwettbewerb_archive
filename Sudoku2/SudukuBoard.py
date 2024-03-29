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



def drawInputTextfield(active:bool, x:int, y:int, width:int, heigth:int):
    input_text = ""
    input_field_rect = pygame.Rect(x,y, width, heigth)
    active = False

    return input_field_rect

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

    def emailundPasswortEingabe(password, email):
        sql = "select email,password from sudoku.user where email = (email) and password = (password) VALUES (%s,%s)"

        try:
            values = (email, password)
            mycursor.execute(sql, values)
        except mysql.connector.errors.ProgrammingError:
            print("wrong username or password")



    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def click(self, event, username:str,age,email,password,phone_number,IP,land):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.change_text(self.feedback, bg="red")
                    print("Username ", username)

                    self.createANewUserInMySQLTable(username,str(age),email,password,phone_number,IP,land)
    def click_2(self,event, email,password):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM user")

        mouse_x, mouse_y = pygame.mouse.get_pos()

        myresult = mycursor.fetchall()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_x,mouse_y):
                for oneuser in myresult:
                    if oneuser[3] == email and oneuser[4] == password:
                        print("Hello World")
                        screen.fill((0,0,0))

                        return False

                    else:
                        self.feedback = "Wrong Password or Email"
                        self.change_text(self.feedback,bg = "red")





    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def createANewUserInMySQLTable(self,name="Max",age = str(random.randint(6,99)),email = "Max.Mustermann@gmail.com",password = str(random.randint(100,99999)) + "!",phone_number = random.randint(11111111,99999999),IP = str(random.randint(100,999)) + "." + str(random.randint(10,99)) + "." + str(random.randint(100,999)) + "." + str(random.randint(10,99)),country = "DE"):
        if name == "":
            name = "Max"
        if age == "":
            age = str(random.randint(6,99))
        if email == "":
            email = "Max.Mustermann@gmail.com"
        if password == "":
            password = str(random.randint(100,99999)) + "!"
        if phone_number == "":
            phone_number = random.randint(11111111,99999999)
        if IP == "":
            IP = str(random.randint(100, 999)) + "." + str(random.randint(10, 99)) + "." + str(
                random.randint(100, 999)) + "." + str(random.randint(10, 99))
        if country == "":
            country = "DE"

        sql = "INSERT INTO user (Name, age,email, password, phone_number, IP, Land) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name,age,email,password,phone_number,IP,country)
        mycursor.execute(sql,values)

        mydb.commit()
        print("User {} was created.".format(values))








