from random import randint
import numpy as np
import pygame

pygame.init()
display = pygame.display.set_mode((3440,1440))
still_on = True
clock = pygame.time.Clock()

class Walker():

    def __init__(self):
        self.pos = np.array([display.get_width()/2, display.get_height()/2])
        self.speed = 70
        self.velocity = np.zeros(2)

    def draw(self):
        pygame.draw.circle(display,(255,255,255),(self.pos.astype("int")), self.get_size())

    def get_size(self):
        size = np.random.random_integers(0,2)
        p = size
        rand = np.random.random_integers(0,2)
        if rand > p:
            return size
        else:
            return 1

    def step(self):
        self.velocity = np.random.random_integers(-self.speed,self.speed,2)
        self.pos += self.velocity

    def check_boundaries(self):
        if self.pos[0] < 0 or self.pos[0] > display.get_width() or self.pos[1] < 0 or self.pos[1] > display.get_height():
            self.pos = np.random.random_integers(0, display.get_width(), 2)

walk = Walker()

walk.draw()


while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "randomwalker_8way.png")

    walk.check_boundaries()
    walk.step()
    walk.draw()
    clock.tick(30)
    pygame.display.update()
