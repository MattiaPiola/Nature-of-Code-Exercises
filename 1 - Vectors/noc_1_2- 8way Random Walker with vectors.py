from random import randint
import numpy as np
import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
still_on = True
clock = pygame.time.Clock()

class Walker():

    def __init__(self):
        self.pos = np.array([display.get_width()/2, display.get_height()/2])
        self.old_pos = np.copy(self.pos)
        self.speed = 20
        self.velocity = np.zeros(2)

    def draw(self):
        pygame.draw.line(display,(255,255,255), self.old_pos.astype("int"), self.pos.astype("int"))

    def step(self):
        self.velocity = np.random.random_integers(-self.speed,self.speed,2)
        self.old_pos = np.copy(self.pos)
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
