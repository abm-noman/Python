import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 10
BOARD_SIZE = 3
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()


def draw_lines():
    # Vertical Lines
    pygame.draw.line(screen, WHITE, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)
    # Horizontal Lines
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)


def draw_board(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)


def draw_x(row, col):
    x = col * WIDTH // BOARD_SIZE + WIDTH // BOARD_SIZE // 2
    y = row * HEIGHT // BOARD_SIZE + HEIGHT // BOARD_SIZE // 2
    offset = WIDTH // BOARD_SIZE // 4
    pygame.draw.line(screen, WHITE, (x - offset, y - offset), (x + offset, y + offset), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (x + offset, y - offset), (x - offset, y + offset), LINE_WIDTH)


def draw_o(row, col):
    x = col * WIDTH // BOARD_SIZE + WIDTH // BOARD_SIZE // 2
    y = row * HEIGHT // BOARD_SIZE + HEIGHT // BOARD_SIZE // 2
    radius = WIDTH // BOARD_SIZE // 4
    pygame.draw.circle(screen, WHITE, (x, y), radius, LINE_WIDTH)


def is_winner(board, player):
    # Check rows
    for row in range(BOARD_SIZE):
        if all(cell == player for cell in board[row]):
            return True

    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False


def is_board_full(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == '':
                return False
    return True


def restart_game():
    return [[''] * BOARD_SIZE for _ in range(BOARD_SIZE)]


# Game Variables
current_player = 'X'
game_board = restart_game()
game_over = False

# Game Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            col = mouseX // (WIDTH // BOARD_SIZE)
            row = mouseY // (HEIGHT // BOARD_SIZE)
            game_board[row][col] = current_player
            if is_winner(game_board, current_player):
                game_over = True
            elif is_board_full(game_board):
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

    # Update the display
    screen.fill(BLACK)
    draw_lines()
    draw_board(game_board)
    pygame.display.flip()

    # Check game over conditions
    if game_over:
        pygame.time.wait(1000)  # Pause for 1 second
        game_board = restart_game()
        game_over = False
        current_player = 'X'

    # Set the FPS
    clock.tick(FPS)
