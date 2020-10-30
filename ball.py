import pygame

class Ball:
    # pass
    #class variables
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, wcolor, bgcolor, CONSTANTS):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.wcolor = wcolor
        self.bgcolor = bgcolor
        self.HEIGHT = CONSTANTS.HEIGHT
        self.BORDER = CONSTANTS.BORDER
        self.WIDTH = CONSTANTS.WIDTH

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        px = self.x + self.vx
        py = self.y + self.vy

        # Collision handling for the ball hitting the top or bottom wall
        if py < self.BORDER + self.RADIUS or py > self.HEIGHT - self.BORDER - self.RADIUS:
            self.vy = -self.vy

        # Collision handling for the ball hitting the left wall
        if px < self.BORDER + self.RADIUS:
            self.vx = -self.vx
        
        # delete the old ball
        self.show(self.bgcolor)

        # np = op + dp
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.wcolor)