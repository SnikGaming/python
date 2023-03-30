import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH = 640
HEIGHT = 480

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game title
pygame.display.set_caption("Snake Game")

# Load snake and food images
snake_img = pygame.image.load("Screenshot 2023-03-30 000410.png").convert_alpha()
food_img = pygame.image.load("Screenshot 2023-03-30 000410.png").convert_alpha()

# Sizes of snake and food
SNAKE_SIZE = snake_img.get_width()
FOOD_SIZE = food_img.get_width()

# Initialize snake and food positions
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
food_x = random.randint(0, WIDTH - FOOD_SIZE)
food_y = random.randint(0, HEIGHT - FOOD_SIZE)

# Initialize snake length
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Initialize snake direction
snake_dx = SNAKE_SIZE
snake_dy = 0

# Score
score = 0

# Initialize font
font = pygame.font.Font(None, 36)

# Game speed
clock = pygame.time.Clock()
FPS = 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
            elif event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = SNAKE_SIZE
                snake_dy = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if snake eats food
    if snake_x + SNAKE_SIZE >= food_x and \
            snake_x <= food_x + FOOD_SIZE and \
            snake_y + SNAKE_SIZE >= food_y and \
            snake_y <= food_y + FOOD_SIZE:
        score += 1
        food_x = random.randint(0, WIDTH - FOOD_SIZE)
        food_y = random.randint(0, HEIGHT - FOOD_SIZE)
        snake_length += 1

    # Add new snake position to the beginning of the list
    snake_body.insert(0, (snake_x, snake_y))

    # If the length of the list is greater than snake_length, remove the last element of the list
    if len(snake_body) > snake_length:
        snake_body.pop()

    # Draw game screen
    screen.fill(WHITE)

    # Draw snake
    for x, y in snake_body:
        screen.blit(snake_img, (x, y))

    # Draw food
    screen.blit(food_img, (food_x, food_y))

    # Show score
    score_text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Adjust game speed
    clock.tick(FPS)

# Quit
