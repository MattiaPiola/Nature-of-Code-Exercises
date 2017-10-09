from random import randint, gauss

import pygame
from math import floor

pygame.init()
display = pygame.display.set_mode((1000,1500))
pygame.display.set_caption("Istogram")
clock = pygame.time.Clock()
number_of_bars = 1000
still_on = True


class Bar():
    def __init__(self, value):
        self.width = display.get_width()/number_of_bars
        self.x = value*self.width
        self.times = 0
        self.speed = 20

    def draw(self):
        pygame.draw.rect(display, (150, 0, 0), (self.x, display.get_height(), self.width, -self.times*self.speed))

    def update_times(self):
        self.times += 1


bars = []

for n in range(0, number_of_bars):
    b = Bar(n)
    bars.append(b)


def randomness():
    randnum = gauss(500,150)
    return randnum


while still_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "screenshot.png")

    r = int(floor(randomness()))
    if r <= len(bars) and r >= 0 :
        bars[r].update_times()


    for b in bars:
        b.draw()

    # clock.tick(250)
    pygame.display.update()
