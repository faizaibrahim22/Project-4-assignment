import pygame
import time
import random

# Pygame ko initialize karna
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
dis_width = 600
dis_height = 400

# Game window set karna
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Faiza')

# Game clock
clock = pygame.time.Clock()

# Snake ki size aur speed
snake_block = 10
snake_speed = 15

# Font aur text setup
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Score display karne ki function
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Snake ka drawing function
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Game over ka function
def game_over_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake ki initial position aur size
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # Snake ka body list aur initial length
    snake_List = []
    Length_of_snake = 1

    # Random position par apple generate karna
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            game_over_message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Key press karte hain
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Agar snake screen ke bahar chale jaaye
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Snake ka position update karna
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Apple ko draw karna
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])

        # Snake ki body update karte hain
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Agar snake apple khata hai
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Speed control karna
        clock.tick(snake_speed)

    # Pygame ko quit karna
    pygame.quit()
    quit()

# Game ko start karna
gameLoop()
