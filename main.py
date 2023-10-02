import sys
import pygame
import numpy as np
from snake import *

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    NUM_ROCKETS = 100
    BRANCHWID = 2
    alpha = 20
    BLACK = 0
    ANGLE = 90
    ITERATION = 9
    rounds = 500
    HEIGHT = 35
    WIDTH = 2
    force = np.arange(-0.01, 0.01, 0.001, dtype=float)
    # Create the screen surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 24)
    snake = Snake()
    food = createFood()
    while (rounds > 0):

        color = (255, 255, 255, alpha) 
        # Clear the screen with a white background
        screen.fill(BLACK)
        display_text(f"Food : ({food.x}, {food.y})", 10, 10, WHITE, font, screen)
        py.draw.rect(screen, "red", food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rounds = 0
            elif event.type == pygame.KEYDOWN:  # Check for a key press event
                if event.key == pygame.K_w:
                    snake.move("w")
                if event.key == pygame.K_a:
                    snake.move("a")
                if event.key == pygame.K_d:
                    snake.move("d")
                if event.key == pygame.K_s:
                    snake.move("s")
        food = snake.update(food, screen, font)
        if food == False:
            rounds = 0
        snake.draw(screen)
        # Update the display
        pygame.display.update()
        pygame.time.delay(100)
        rounds -= 1
    
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
