import pygame
import random

# initialize Pygame
pygame.init()

# set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set up the game clock
clock = pygame.time.Clock()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up the fonts
font = pygame.font.SysFont(None, 36)

# set up the Pac-Man and the ghosts
pacman_image = pygame.image.load("pacman.png")
pacman_rect = pacman_image.get_rect()
pacman_rect.x = 400
pacman_rect.y = 300

ghost_image = pygame.image.load("ghost.png")
ghost_rect = ghost_image.get_rect()
ghost_rect.x = random.randint(0, screen_width - ghost_rect.width)
ghost_rect.y = random.randint(0, screen_height - ghost_rect.height)

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_rect.x -= 5
    elif keys[pygame.K_RIGHT]:
        pacman_rect.x += 5
    elif keys[pygame.K_UP]:
        pacman_rect.y -= 5
    elif keys[pygame.K_DOWN]:
        pacman_rect.y += 5

    # update the game state
    ghost_rect.x += random.randint(-5, 5)
    ghost_rect.y += random.randint(-5, 5)

    # handle collisions
    if pacman_rect.colliderect(ghost_rect):
        text = font.render("Game Over!", True, RED)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # draw the screen
    screen.fill(BLACK)
    screen.blit(pacman_image, pacman_rect)
    screen.blit(ghost_image, ghost_rect)
    pygame.display.flip()

    # update the game clock
    clock.tick(60)

# quit Pygame
pygame.quit()
