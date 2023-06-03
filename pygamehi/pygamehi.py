import pygame
import sudoku_board as sdk8
pygame.init()

screen = pygame.display.set_mode([800,700])
button_new_user = sdk8.Button("Click here", (100,100), font = 30,bg="navy",feedback="You just clicked me")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button_new_user.click(event)
    clock = pygame.time.Clock()
    print("event type:" , event.type)

    button_new_user.show()
    print("clocl:" , clock)

    button_new_user.show()

    sdk8.drawCircle(screen)
    pygame.display.flip()



pygame.quit()

