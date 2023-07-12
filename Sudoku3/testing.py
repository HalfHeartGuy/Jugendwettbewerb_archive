import pygame
import sys

pygame.init()

# Fenstergröße
WIDTH = 400
HEIGHT = 300

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Erstellen des Fensters
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")

# Schriftart initialisieren
font = pygame.font.Font(None, 48)

# Timer-Werte
timer_value = 0  # 60 Sekunden
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # Timer-Ereignis alle 1000ms (1 Sekunde) auslösen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            timer_value += 1
            if timer_value == 0:
                pygame.time.set_timer(timer_event, 0)  # Timer-Ereignis stoppen, wenn der Countdown abgelaufen ist

    # Hintergrund löschen
    window.fill(BLACK)

    # Timer-Text rendern
    timer_text = font   .render(str(timer_value), True, WHITE)
    timer_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Timer-Text zeichnen
    window.blit(timer_text, timer_rect)

    # Bildschirm aktualisieren
    pygame.display.flip()
