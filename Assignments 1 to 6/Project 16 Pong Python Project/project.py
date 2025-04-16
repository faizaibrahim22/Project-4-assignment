import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width = 15
paddle_height = 100

# Ball dimensions
ball_radius = 10

# Paddle positions
paddle1_y = (screen_height - paddle_height) // 2
paddle2_y = (screen_height - paddle_height) // 2

# Ball position and speed
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = random.choice([1, -1]) * 5
ball_dy = random.choice([1, -1]) * 5

# Speed of paddles
paddle_speed = 7

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball bouncing off the top and bottom
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_dy = -ball_dy

    # Ball bouncing off paddles
    if ball_x - ball_radius <= paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_dx = -ball_dx
    if ball_x + ball_radius >= screen_width - paddle_width and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_dx = -ball_dx

    # Ball reset if out of bounds
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = random.choice([1, -1]) * 5
        ball_dy = random.choice([1, -1]) * 5

    # Drawing everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (10, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (screen_width - 10 - paddle_width, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, white, (0, 0, screen_width, screen_height), 5)

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
