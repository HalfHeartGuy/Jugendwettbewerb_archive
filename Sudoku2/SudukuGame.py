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

####  inputfiled: age #######################
input_age_rect = sdkB.drawInputTextfield(active, 200, 250, 150, 30)
input_age = ""
# inputfeld: email
input_email_rect = sdkB.drawInputTextfield(active,200,300,150,30)
input_email = ""

#inputfeld:passwort
input_password_rect = sdkB.drawInputTextfield(active,200,350,150,30)
input_password = ""
#input field_phone_number
input_phonenumber_rect = sdkB.drawInputTextfield(active,200,400,150,30)
input_phonenumber = ""

#input field:IP
input_IP_rect = sdkB.drawInputTextfield(active,200,450,150,30)
input_IP = ""


#input field:Land
input_land_rect = sdkB.drawInputTextfield(active,200,500,150,30)
input_land = ""

input_text_font = pygame.font.Font(None, 32)
#### here the end of code for input box


selected_input_field = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        button_new_user.click(event, input_username, input_age,input_email,input_password,input_phonenumber,input_IP,input_land)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_username_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_username_rect"
            elif input_age_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_age_rect"
            elif input_email_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_email_rect"
            elif input_password_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_password_rect"
            elif input_phonenumber_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_phonenumber_rect"
            elif input_IP_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_IP_rect"
            elif input_land_rect.collidepoint(event.pos):
                active = True
                selected_input_field = "input_land_rect"

            else:
                active = False


        if event.type == pygame.KEYDOWN:
            if selected_input_field == "input_username_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_username = input_username[:-1]
                elif event.key == pygame.K_DELETE:
                    input_username = ""
                input_username += event.unicode

            elif selected_input_field == "input_age_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_age = input_age[:-1]
                elif event.key == pygame.K_DELETE:
                    input_age = ""
                input_age += event.unicode
            elif selected_input_field == "input_email_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_email = input_email[:-1]
                elif event.key == pygame.K_DELETE:
                    input_email = ""
                input_email += event.unicode
            elif selected_input_field == "input_password_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_password = input_password[:-1]
                elif event.key == pygame.K_DELETE:
                    input_password = ""
                input_password += event.unicode
            elif selected_input_field == "input_phonenumber_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_phonenumber = input_phonenumber[:-1]
                elif event.key == pygame.K_DELETE:
                    input_phonenumber = ""
                input_phonenumber += event.unicode
            elif selected_input_field == "input_IP_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_IP = input_IP[:-1]
                elif event.key == pygame.K_DELETE:
                    input_IP = ""
                input_IP += event.unicode
            elif selected_input_field == "input_land_rect":
                if event.key == pygame.K_BACKSPACE:
                    input_land = input_land[:-1]
                elif event.key == pygame.K_DELETE:
                    input_land = ""
                input_land += event.unicode




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

    ##### Zeichen von Age
    pygame.draw.rect(screen, color_input_field, input_age_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_age, True, (255, 255, 255))
    screen.blit(text_surface, (input_age_rect.x + 5, input_age_rect.y + 5))
    # Inputfield width would be updated
    input_age_rect.w = max(100, text_surface.get_width())

    #Zeichnen von email
    pygame.draw.rect(screen, color_input_field, input_email_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_email, True, (255, 255, 255))
    screen.blit(text_surface, (input_email_rect.x + 5, input_email_rect.y + 5))
    # Inputfield width would be updated
    input_email_rect.w = max(100, text_surface.get_width())
    #Zeichen von Passwort
    pygame.draw.rect(screen, color_input_field, input_password_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_password, True, (255, 255, 255))
    screen.blit(text_surface, (input_password_rect.x + 5, input_password_rect.y + 5))
    # Inputfield width would be updated
    input_password_rect.w = max(100, text_surface.get_width())

    #Zeichenn von Phone Number
    pygame.draw.rect(screen, color_input_field, input_phonenumber_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_phonenumber, True, (255, 255, 255))
    screen.blit(text_surface, (input_phonenumber_rect.x + 5, input_phonenumber_rect.y + 5))
    # Inputfield width would be updated
    input_phonenumber_rect.w = max(100, text_surface.get_width())

    #Zeichen von IP
    pygame.draw.rect(screen, color_input_field, input_IP_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_IP, True, (255, 255, 255))
    screen.blit(text_surface, (input_IP_rect.x + 5, input_IP_rect.y + 5))
    # Inputfield width would be updated
    input_IP_rect.w = max(100, text_surface.get_width())
    #Zeichnen von land
    pygame.draw.rect(screen, color_input_field, input_land_rect)
    # here the code for draw of input text
    text_surface = input_text_font.render(input_land, True, (255, 255, 255))
    screen.blit(text_surface, (input_land_rect.x + 5, input_land_rect.y + 5))
    # Inputfield width would be updated
    input_land_rect.w = max(100, text_surface.get_width())



pygame.quit()



