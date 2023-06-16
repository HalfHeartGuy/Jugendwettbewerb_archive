import pygame
import SudukuBoard as sdkB
from pygame import Surface
from SudukuBoard import *

pygame.init()
screen = pygame.display.set_mode([800,600])
keystate = pygame.key.get_pressed()

button_new_user = sdkB.Button( "Click here", (100,100), font=30, bg="navy", feedback="You just clicked me")



clock = pygame.time.Clock()


# here code for input box
color_input_field = None
active = False
color_passive = pygame.Color("chartreuse4")
color_active = pygame.Color("lightskyblue3")
input_field_rect = drawInputTextfield(active)
sdkB.drawInputTextfield(active)
#here the end of code for input box
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        button_new_user.click(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_field_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

    button_new_user.show()
    clock.tick(30)
    pygame.display.update()

    button_new_user.show()
    #
    if active:
        color_input_field = color_active
    else:
        color_input_field = color_passive
    pygame.draw.rect(screen,color_input_field,input_field_rect)




  #  sdkB.drawCircle(screen)

pygame.quit()



