# tetris.py
import pygame
import random

# Define game constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = RED
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

def draw_grid(screen):
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris by Faiza")
    clock = pygame.time.Clock()
    run = True

    current_piece = Piece(3, 0, [random.choice(SHAPES)])

    while run:
        screen.fill(BLACK)
        draw_grid(screen)

        shape_format = current_piece.image()
        for i, row in enumerate(shape_format):
            for j, column in enumerate(row):
                if column:
                    pygame.draw.rect(
                        screen,
                        current_piece.color,
                        pygame.Rect((current_piece.x + j) * BLOCK_SIZE,
                                    (current_piece.y + i) * BLOCK_SIZE,
                                    BLOCK_SIZE, BLOCK_SIZE)
                    )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
