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

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

# Define car image and position
car_image = pygame.image.load("E:\Gift for chiina\china wall papers HD 4K\china wallpapers (2).jpg")  # Replace "car.png" with your car image path
car_rect = car_image.get_rect()
car_rect.center = (WIDTH // 2, HEIGHT // 2)

# Define road image and position
road_image = pygame.image.load("E:\AddText_01-16-08.43.59.jpg")  # Replace "road.png" with your road image path
road_rect = road_image.get_rect()
road_rect.y = 0

# Define obstacles list
obstacles = []

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control car movement with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_rect.move_ip(-10, 0)
            elif event.key == pygame.K_RIGHT:
                car_rect.move_ip(10, 0)
            elif event.key == pygame.K_UP:
                car_rect.move_ip(0, -10)
            elif event.key == pygame.K_DOWN:
                car_rect.move_ip(0, 10)

    # Move road image continuously
    road_rect.y += 5
    if road_rect.y >= HEIGHT:
        road_rect.y = 0

    # Spawn and move obstacles
    if random.randint(0, 100) < 5:
        obstacle_rect = pygame.Rect(random.randint(0, WIDTH - 50), road_rect.y - 50, 50, 50)
        obstacles.append(obstacle_rect)
    for obstacle in obstacles:
        obstacle.y += 5
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

    # Check for collision with obstacles
    for obstacle in obstacles:
        if car_rect.colliderect(obstacle):
            running = False

    # Draw screen
    screen.fill(BLACK)
    screen.blit(road_image, road_rect)
    screen.blit(car_image, car_rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Update display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
