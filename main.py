import pygame

# Init pygame
pygame.init()

# Create window
window = pygame.display.set_mode((800, 600))

# Game loop
is_running = True
while is_running:
    for event in pygame.event.get():
        # End the program and close the window if 'X' window decoration is clicked
        if event.type == pygame.QUIT:
            is_running = False
