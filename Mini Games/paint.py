import pygame
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption("Paint")

# Set the background color
screen.fill(WHITE)

# Set the default color
color = BLACK

# Set the default thickness
thickness = 1

# Set the flag for drawing
drawing = False

# Set the clock
clock = pygame.time.Clock()

# Main loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_w:
                color = WHITE
            elif event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_s:
                # Save the image
                pygame.image.save(screen, "image.png")
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                thickness += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                thickness -= 1
                if thickness < 1:
                    thickness = 1

    # Draw on the screen
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, pos, thickness)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
