import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
width = 400
height = 200

# Create the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Box")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the text and font
text = "Hello, world!"
font = pygame.font.SysFont(None, 40)

# Render the text
text_surface = font.render(text, True, BLACK)

# Calculate the dimensions of the box
box_width = text_surface.get_width() + 20
box_height = text_surface.get_height() + 20

# Calculate the position of the box
box_x = (width - box_width) // 2
box_y = (height - box_height) // 2

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(WHITE)

    # Draw the box
    pygame.draw.rect(window, BLACK, (box_x, box_y, box_width, box_height))

    # Draw the text
    text_x = box_x + (box_width - text_surface.get_width()) // 2
    text_y = box_y + (box_height - text_surface.get_height()) // 2
    window.blit(text_surface, (text_x, text_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
