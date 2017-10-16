from random import randint

import pygame
import numpy as np
from noise._perlin import noise1

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()


class Balloon():
    def __init__(self, x=400, y=600):
        self.pos = np.array([x, y], dtype="float32")
        self.velocity = np.zeros(2, dtype="float32")
        self.acceleration = np.zeros(2,  dtype="float32")
        self.size = 25
        self.outer_col = [randint(0, 205), randint(0, 205), randint(0, 205)]
        self.inner_col = np.add(self.outer_col, [50, 50, 50])

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0

    def draw(self, wind):
        pygame.draw.circle(display, (self.inner_col), self.pos, self.size)
        pygame.draw.circle(display, (self.outer_col), self.pos, self.size, 3)
        pygame.draw.line(display, (255, 255, 255), self.pos + [0, self.size], self.pos + [0, 2*self.size] + wind, 5)

    def apply_force(self, force):
        self.acceleration += force

    def check_boundaries(self):
        i = 0
        while i < 2:
            if self.pos[i] - self.size*3 > 800:
                self.pos[i] = 0
            elif self.pos[i] + self.size*3 < 0:
                self.pos[i] = 800

            i += 1

balls = []

balloon = Balloon()
balls.append(balloon)
time = 0

helium = np.array([0,-.08])
balloon.apply_force(helium)



while still_on:
    display.fill((188,242,253))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            balloon = Balloon(x = randint(0, 800))
            balloon.apply_force(helium)
            balls.append(balloon)
            # pygame.image.save(display, "screenshot.png")


    wind = np.array([noise1(time/2, octaves=3),0])

    for balloon in balls:
        balloon.apply_force(wind)
        balloon.update()
        balloon.check_boundaries()
        balloon.draw(wind)

    time += 1
    # clock.tick(60)
    pygame.display.update()
