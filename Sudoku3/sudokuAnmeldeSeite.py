import pygame
import mysql.connector
import sudoku_2
from sudoku_2 import *
import SudukuBoard as sdkB
from SudukuBoard import *
import math
from math import *
pygame.init()
screen = pygame.display.set_mode([800,600])
keystate = pygame.key.get_pressed()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "sudoku"
)


button_drawing = True

clock = pygame.time.Clock()

#### here  the code for input box



color_input_field = None
active = False
color_passive = pygame.Color('chartreuse4')
color_active = pygame.Color('lightskyblue3')

###  inputfield: username ############################
input_email_rect = sdkB.drawInputTextfield(active, 200, 200, 150, 30)
input_email = ""

####  inputfiled: age #######################
input_password_rect = sdkB.drawInputTextfield(active, 200, 250, 150, 30)
input_password = ""
#inputfield:difficulty
input_difficulty_rect = sdkB.drawInputTextfield(active,200,300,150,30)
input_difficulty = ""

#inputfields sudoku 9x9
input_numbers_rect = sdkB.draw9x9SudokuBox(active,50,50,40,40)
print(input_numbers_rect)
input_numbers = zerosInSudoku()



#button start
input_start_rect = sdkB.Button("Click here", (100,100), font=30, bg="navy", feedback="You just clicked me")


input_text_font = pygame.font.Font(None, 32)
#### here the end of code for input box


selected_input_field = ""


#timer
timer_rect = sdkB.drawInputTextfield(active,400,100,150,30)
timer_value = 0
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)


BLACK = (0, 0, 0)

pygame.display.set_caption("Sudoku")



def emailundPasswortEingabe(password,email):



        print("Hello world")#Buttons müssen verschwinden





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == timer_event and button_drawing == False:
            timer_value += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_email_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_email_rect"
            elif input_password_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_password_rect"
            elif input_difficulty_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_difficulty_rect"




            else:
                active = False
        rueckgabeFeld = input_start_rect.click_2(event, input_email, input_password)
        if rueckgabeFeld == False:

            button_drawing = False


        if event.type == pygame.KEYDOWN:
            if selected_input_field == "input_email_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_username = input_email[:-1]
                elif event.key == pygame.K_DELETE:
                    input_username = ""
                input_email += event.unicode

            elif selected_input_field == "input_password_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_age = input_password[:-1]
                elif event.key == pygame.K_DELETE:
                    input_age = ""
                input_password += event.unicode
            elif selected_input_field == "input_difficulty_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_difficulty = input_difficulty[:-1]
                elif event.key == pygame.K_DELETE:
                    input_age = ""
                input_difficulty += event.unicode






    clock.tick(30)
    pygame.display.update()

    if button_drawing == True:
        input_start_rect.show()

        #  here the code for draw of inputfield
        if active:
            color_input_field = color_active
        else:
            color_input_field = color_passive

        # Zeichnen des Eingabesfeldes email"
        pygame.draw.rect(screen, color_input_field, input_email_rect)
        # here the code for draw of input text
        text_surface = input_text_font.render(input_email, True, (255, 255, 255))
        screen.blit(text_surface, (input_email_rect.x + 5, input_email_rect.y + 5))
        # Inputfield width would be updated
        input_email_rect.w = max(100, text_surface.get_width())

        ##### Zeichen von password
        pygame.draw.rect(screen, color_input_field, input_password_rect)
        # here the code for draw of input text
        text_surface = input_text_font.render(input_password, True, (255, 255, 255))
        screen.blit(text_surface, (input_password_rect.x + 5, input_password_rect.y + 5))
        # Inputfield width would be updated
        input_password_rect.w = max(100, text_surface.get_width())


        #Zeichen von difficulty
        pygame.draw.rect(screen, color_input_field, input_difficulty_rect)
        # here the code for draw of input text
        text_surface = input_text_font.render(input_difficulty, True, (255, 255, 255))
        screen.blit(text_surface, (input_difficulty_rect.x + 5, input_difficulty_rect.y + 5))
        # Inputfield width would be updated
        input_difficulty_rect.w = max(100, text_surface.get_width())
    else:

        timer_rect = pygame.Rect(600, 100, 150, 30)
        pygame.draw.rect(screen, (255, 255, 255), timer_rect)
        timer_text = input_text_font.render(str(timer_value), True, (0, 0, 0))
        screen.blit(timer_text, (timer_rect.x + 5, timer_rect.y + 5))

        #Hier fängt draw sudoku an
        for i in range(0, 81):
            if i == 0:
                x = 0
                y = 0
            if i < 9:
                x = 0
                y = i
            else:
                x = i // 9
                y = i % 9


            pygame.draw.rect(screen,color_input_field,input_numbers_rect[i])
            text_surface = input_text_font.render(str(input_numbers[x][y]),True,(255,0,0))
            screen.blit(text_surface, (input_numbers_rect[i]))
            input_numbers_rect[i].w = max(1, text_surface.get_width())




pygame.quit()


