import pygame
import numpy as np

pygame.init()
display = pygame.display.set_mode((800,800))
pygame.display.set_caption("Spiral")
clock = pygame.time.Clock()
stillOn = True

class Ball():
    def __init__(self):
        self.ro = 0
        self.theta = 0
        self.center = [400,400]

    def update(self):
        self.theta += 0.01
        self.ro += 0.05

    def draw(self):
        x = self.ro * np.cos(self.theta) + self.center[0]
        y = self.ro * np.sin(self.theta) + self.center[1]
        pygame.draw.circle(display, (255,255,255), (int(x),int(y)), 3)

ball = Ball()

while stillOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stillOn = False

    ball.update()
    ball.draw()

    # clock.tick(60)
    pygame.display.update()
