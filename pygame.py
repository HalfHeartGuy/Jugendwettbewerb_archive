import pygame
scr = pygame.display.set_mode((640,480))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        scr.fill(255,255,255)
        pygame.draw.circle(scr, (0,0,0), (400,300),100)
        pygame.display.update()

pygame.quit()