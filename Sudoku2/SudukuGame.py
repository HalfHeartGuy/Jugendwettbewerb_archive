import pygame
import SudukuBoard as sdkB
from pygame import Surface
from SudukuBoard import *

pygame.init()
screen = pygame.display.set_mode([800,600])
keystate = pygame.key.get_pressed()

button_new_user = sdkB.Button( "Click here", (100,100), font=30, bg="navy", feedback="You just clicked me")



clock = pygame.time.Clock()

#### here  the code for input box
color_input_field = None
active = False
color_passive = pygame.Color('chartreuse4')
color_active = pygame.Color('lightskyblue3')

###  inputfield: username ############################
input_username_rect = sdkB.drawInputTextfield(active, 200, 200, 150, 30)
input_username = ""

####  inputfiled: password #######################
input_password_rect = sdkB.drawInputTextfield(active, 200, 300, 150, 30)
input_password = ""



input_text_font = pygame.font.Font(None, 32)
#### here the end of code for input box


selected_input_field = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        button_new_user.click(event, input_username)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_username_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_username_rect"
            elif input_password_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_password_rect"
            else:
                active = False


        if event.type == pygame.KEYDOWN:
            if selected_input_field == "input_username_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_username = input_username[:-1]
                elif event.key == pygame.K_DELETE:
                    input_username = ""
                input_username += event.unicode

            elif selected_input_field == "input_password_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_password = input_password[:-1]
                elif event.key == pygame.K_DELETE:
                    input_password = ""
                input_password += event.unicode

    button_new_user.show()
    clock.tick(30)
    pygame.display.update()

    button_new_user.show()

  #  here the code for draw of inputfield
    if active:
        color_input_field = color_active
    else:
        color_input_field = color_passive

    # Zeichnen des Eingabesfeldes "Username"
    pygame.draw.rect(screen, color_input_field, input_username_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_username, True, (255, 255, 255))
    screen.blit(text_surface, (input_username_rect.x + 5, input_username_rect.y + 5))
    # Inputfield width would be updated
    input_username_rect.w = max(100, text_surface.get_width())

    ##### Zeichen von Passwordeingabe
    pygame.draw.rect(screen, color_input_field, input_password_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_password, True, (255, 255, 255))
    screen.blit(text_surface, (input_password_rect.x + 5, input_password_rect.y + 5))
    # Inputfield width would be updated
    input_password_rect.w = max(100, text_surface.get_width())



pygame.quit()



