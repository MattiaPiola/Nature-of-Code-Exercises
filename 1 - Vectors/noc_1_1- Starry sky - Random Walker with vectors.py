from random import randint
import numpy as np
import pygame

pygame.init()
display = pygame.display.set_mode((3440,1440))
still_on = True
clock = pygame.time.Clock()

class Walker():

    def __init__(self, color):
        self.pos = np.array([display.get_width()/2, display.get_height()/2])
        self.speed = 120
        self.velocity = np.zeros(2)
        self.color = color

    def draw(self):
        pygame.draw.circle(display,self.color,(self.pos.astype("int")), self.get_size())

    def get_size(self):
        size = np.random.random_integers(0,4)
        p = size
        rand = np.random.random_integers(0,4)
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

walkers =[]
walk1 = Walker((195,170,130))
walk2 = Walker((205,180,255))
walk3 = Walker((255,255,255))
walk4 = Walker((150,150,255))
walkers.append(walk1)
walkers.append(walk2)
walkers.append(walk3)
walkers.append(walk4)



while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "randomwalker_8way.png")

    for walk in walkers:
        walk.check_boundaries()
        walk.step()
        walk.draw()
    clock.tick(30)
    pygame.display.update()
