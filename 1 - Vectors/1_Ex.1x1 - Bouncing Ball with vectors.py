import pygame
import numpy as np

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()

class Ball():
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.speed = np.random.random_integers(0,10,2)

    def update_pos(self):
        self.pos += self.speed


    def check_boundaries(self):
        if self.pos[0] < 0 or self.pos[0] > display.get_width():
            self.speed *= [-1,1]
        if self.pos[1] < 0 or self.pos[1] > display.get_height():
            self.speed *= [1,-1]

    def draw(self):
        pygame.draw.circle(display, (255,0,0), (self.pos), 20)

    def gravity(self):
        self.speed += [0,10]



ball = Ball(400, 200)


while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")

    ball.gravity()
    ball.update_pos()
    ball.check_boundaries()
    ball.draw()


    clock.tick(60)
    pygame.display.update()
