import pygame

# define main function
def main():
    pygame.init()
    pygame.display.set_caption("my pong")

    WIDTH = 800
    HEIGHT = 400

    # surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))

    # Walls
    # Rect(surface, color, rect) -> Rect
    # Rect((left, top), (width, height)) -> Rect
    wcolor = pygame.Color("white")
    BORDER = 15

    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, BORDER)))

    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))

    # bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT - BORDER), (WIDTH, BORDER)))

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    # call the main function
    main()