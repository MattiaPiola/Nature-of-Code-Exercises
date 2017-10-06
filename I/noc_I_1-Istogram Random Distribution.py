from random import randint

import pygame

pygame.init()
display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Istogram")
clock = pygame.time.Clock()
still_on = True


class Bar():
    def __init__(self, value):
        self.x = value*100
        self.times = 0

    def draw(self):
        pygame.draw.rect(display, (255, 255, 255), (self.x, display.get_height(), 100, -self.times))

    def update_times(self):
        self.times += 1


bars = []

for n in range(0, 10):
    b = Bar(n)
    bars.append(b)


def randomness():
    randnum = randint(0, 9)
    return randnum


while still_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False

    r = randomness()
    bars[r].update_times()

    for b in bars:
        b.draw()

    clock.tick(30)
    pygame.display.update()
