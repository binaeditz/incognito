import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen size
WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Define snake body as a list of coordinates
snake_body = [[400, 300], [400, 310], [400, 320]]

# Define snake direction
snake_direction = "RIGHT"

# Define food position
food_pos = [random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10)]

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Change snake direction based on key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Update snake head position based on direction
    if snake_direction == "UP":
        snake_body.insert(0, [snake_body[0][0], snake_body[0][1] - 10])
    elif snake_direction == "DOWN":
        snake_body.insert(0, [snake_body[0][0], snake_body[0][1] + 10])
    elif snake_direction == "LEFT":
        snake_body.insert(0, [snake_body[0][0] - 10, snake_body[0][1]])
    elif snake_direction == "RIGHT":
        snake_body.insert(0, [snake_body[0][0] + 10, snake_body[0][1]])

    # Check for collision with walls or self
    if (snake_body[0][0] < 0 or snake_body[0][0] > WIDTH - 10 or
        snake_body[0][1] < 0 or snake_body[0][1] > HEIGHT - 10 or
        snake_body[0] in snake_body[1:]):
        running = False

    # Check for food collision
    if snake_body[0] == food_pos:
        # Grow snake and spawn new food
        snake_body.append([snake_body[-1][0], snake_body[-1][1]])
        food_pos = [random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10)]

    # Draw screen
    screen.fill(BLACK)

    # Draw snake
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update display
    pygame.display.flip()

    # Control game speed
    clock.tick(6)

# Quit Pygame
pygame.quit()
