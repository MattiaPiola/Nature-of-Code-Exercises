from random import gauss

import pygame
from math import floor

from numpy.ma.core import subtract

pygame.init()
display = pygame.display.set_mode((2000, 1000))
still_on = True
clock = pygame.time.Clock()

class PaintDrop():

    def __init__(self):
        self.x = int(floor((gauss(display.get_width()/2, display.get_width()/10))))
        self.y = int(floor(gauss(display.get_height()/2, display.get_height()/10)))
        self.color = [self.get_color(255,3), self.get_color(255,3), self.get_color(255,3)]
        self.size = int(floor(gauss(display.get_width()/40, display.get_width()/300)))

    def get_color(self, mu, sigma):
        correct = False
        while correct == False:
            color = int(floor(gauss(mu, sigma)))
            if color > 0 and color < 255:
                correct = True
        return color

    def draw(self):
        pygame.draw.circle(display,self.color,(self.x, self.y), self.size)
        pygame.draw.circle(display, subtract(self.color,[20, 20, 20]), (self.x, self.y), self.size, 2)


drops = 0
display.fill((150, 100, 0))

while still_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "screenshot.png")

    # while drops < 50:
    drop = PaintDrop()
    drop.draw()
    drops += 1

    clock.tick(5)
    pygame.display.update()
