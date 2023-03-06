import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the font and font size
font = pygame.font.SysFont(None, 25)

# Define the block size of the snake and the food
BLOCK_SIZE = 10

# Set the clock
clock = pygame.time.Clock()

def draw_snake(snake_list):
    """Draw the snake on the screen"""
    for x,y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color):
    """Display a message on the screen"""
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH/6, HEIGHT/3])

def gameLoop():
    """The main game loop"""
    game_exit = False
    game_over = False

    # Set the starting position of the snake
    lead_x = WIDTH/2
    lead_y = HEIGHT/2
    lead_x_change = 0
    lead_y_change = 0

    # Set the starting position of the food
    food_x = round(random.randrange(0, WIDTH-BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT-BLOCK_SIZE) / 10.0) * 10.0

    # Create an empty list for the snake
    snake_list = []
    snake_length = 1

    while not game_exit:

        while game_over == True:
            screen.fill(WHITE)
            message("Game over, press Q to quit or C to play again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        # Check if the snake hits the boundaries of the screen
        if lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0:
            game_over = True

        # Update the position of the snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Add the head of the snake to the beginning of the snake_list
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw the snake
        draw_snake(snake_list)

        # Update the snake length and the position of the food
        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, WIDTH-BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT-BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        # Set the speed of the game
        clock.tick(15)

    # Quit Pygame
    pygame.quit()

# Call the gameLoop function to start the game
gameLoop()

