import pygame as py
from random import choice
from math import sqrt
# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_DIMENSION = 20
WHITE = (255, 255, 255)
FOODPOSITIONX = list(range(BLOCK_DIMENSION, SCREEN_WIDTH - BLOCK_DIMENSION, BLOCK_DIMENSION))
FOODPOSITIONY = list(range(BLOCK_DIMENSION, SCREEN_HEIGHT - BLOCK_DIMENSION, BLOCK_DIMENSION))

# Function to display text on the screen
def display_text(text, x, y, color, font, screen):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def createFood():
    return py.Rect(choice(FOODPOSITIONX), choice(FOODPOSITIONY), BLOCK_DIMENSION, BLOCK_DIMENSION)

class Snake:
    
    def __init__(self):

        self.height = BLOCK_DIMENSION
        self.width = BLOCK_DIMENSION
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT - self.height - 2 * BLOCK_DIMENSION
        self.xdir = 0
        self.ydir = 0
        self.color = WHITE
        self.body = [py.Rect(self.x, self.y, self.width, self.height),
                    py.Rect(self.x, self.y + BLOCK_DIMENSION, self.width, self.height)]

    def draw(self, screen):
        for body in self.body:
            py.draw.rect(screen, self.color, body)

    def move(self, key):
        print(f"move called {key}")
        
        if key == "w":
            self.xdir = 0
            self.ydir = -BLOCK_DIMENSION
        elif key == "s":
            self.xdir = 0
            self.ydir = BLOCK_DIMENSION
        elif key == "a":
            self.xdir = -BLOCK_DIMENSION
            self.ydir = 0
        elif key == "d":
            self.xdir = BLOCK_DIMENSION
            self.ydir = 0

    def eat(self, food):
         
        x = self.body[0].x
        y = self.body[0].y

        if x == food.x and y == food.y:
            return True
        return False

    def grow(self):
        
        oldHead = self.body[0]
        newHead = py.Rect(oldHead.x + self.xdir, oldHead.y + self.ydir, BLOCK_DIMENSION, BLOCK_DIMENSION)
        self.body.insert(0,newHead)
    
    def update(self, food, screen, font):
                    
        # stop snake on colision with boundary
        if self.body[0].x <= 0 or self.body[0].x >= (SCREEN_WIDTH - self.width) or self.body[0].y <= 0 or self.body[0].y >= (SCREEN_HEIGHT - self.height):
        
            self.xdir = self.ydir = 0
            return False
        
        if self.eat(food):
            self.grow()
            food = createFood()

        # add a new-head of the snake in position (old-head + xdir , old-head + ydir)
        # pop the last body of snake
        
        oldHead = self.body[0]
        newHead = py.Rect(oldHead.x + self.xdir, oldHead.y + self.ydir, BLOCK_DIMENSION, BLOCK_DIMENSION)
        self.body.insert(0,newHead)
        self.body.pop()

        display_text(f"Snake head : ({self.body[0].x}, {self.body[0].y})", 10, 30, WHITE, font, screen)
        display_text(f"Snake length : {len(self.body)}", 10, 50, WHITE, font, screen)
        return food

        
        