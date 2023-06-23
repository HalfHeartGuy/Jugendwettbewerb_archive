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
input_txt = ""
input_list = []
input_text_font = pygame.font.Font(None, 32)

#here the end of code for input box
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(input_list) == 0:

                button_new_user.click(event)
            elif len(input_list) == 1:
                button_new_user.click(event,input_list[0])
            elif len(input_list) == 2:
                button_new_user.click(event,input_list[0],input_list[1])
            elif len(input_list) == 3:
                button_new_user.click(event,input_list[0],input_list[1],input_list[2])
            elif len(input_list) == 4:
                button_new_user.click(event,input_list[0],input_list[1],input_list[2],input_list[3])
            elif len(input_list) == 5:
                button_new_user.click(event,input_list[0],input_list[1],input_list[2],input_list[3],input_list[4])


            elif len(input_list) == 6:
                button_new_user.click(event,input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5])

            elif len(input_list) == 7:
                button_new_user.click(event,input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5],input_list[6])




            if input_field_rect.collidepoint(event.pos):
                active = True
            else:
                active = False


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                input_txt = input_txt[:-1]
            input_txt += event.unicode
        print(input_list)
        if input_txt.find(",") != 0:
            input_list = input_txt.split(",")





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
    #here the code for draw of input text
    text_surface = input_text_font.render(input_txt,True,(255,255,255))
    screen.blit(text_surface,(input_field_rect.x + 5, input_field_rect.y + 5))

    #inputfield width would be updated
pygame.quit()



