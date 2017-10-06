from random import randint

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
still_on = True
clock = pygame.time.Clock()

class Walker():

    def __init__(self):
        self.x = display.get_width()/2
        self.y = display.get_height()/2
        self.speed = 1

    def draw(self):
        pygame.draw.line(display,(255,255,255),(self.x, self.y),(self.x, self.y))

    def step(self):
        step = randint(0, 3)
        if step == 0:
            self.x -= self.speed
        elif step == 1:
            self.y -= self.speed
        elif step == 2:
            self.x += self.speed
        elif step == 3:
            self.y += self.speed



walk = Walker()

walk.draw()


while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False

    walk.step()
    walk.draw()
    clock.tick(60)
    pygame.display.update()
