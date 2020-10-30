from paddle import Paddle
from ball import Ball
import pygame
import random
from collections import namedtuple

# define main function
def main():
    pygame.init()
    pygame.display.set_caption("my pong")

    wcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 60

    # Store constants in a tuple
    MyConstants = namedtuple("MyConstants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
    CONSTANTS = MyConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)

    # surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))

    # Walls
    # Rect(surface, color, rect) -> Rect
    # Rect((left, top), (width, height)) -> Rect

    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, BORDER)))

    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))

    # bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT - BORDER), (WIDTH, BORDER)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = random.randint(-VELOCITY, VELOCITY)
    b0 = Ball(x0, y0, vx0, vy0, screen, wcolor, bgcolor, CONSTANTS)
    b0.show(wcolor)

    pygame.display.update()
    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # Event handling
        for event in pygame.event.get():
            # Stops the game if the even is quit
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)

        #Ball update
        b0.update()

if __name__=="__main__":
    # call the main function
    main()