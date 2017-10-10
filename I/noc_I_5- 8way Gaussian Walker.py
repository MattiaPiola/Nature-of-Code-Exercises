from random import randint, gauss

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
still_on = True
clock = pygame.time.Clock()

class Walker():

    def __init__(self):
        self.x = display.get_width()/2
        self.y = display.get_height()/2
        self.past_x = self.x
        self.past_y = self.y
        self.speed = 30

    def draw(self):
        pygame.draw.line(display,(255,255,255),(self.past_x, self.past_y),(self.x, self.y))

    def step(self):
        step_x = gauss(0, 0.3)*self.speed
        step_y = gauss(0, 0.3)*self.speed
        self.past_x = self.x
        self.past_y = self.y
        self.x += step_x
        self.y += step_y



walk = Walker()


while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "gaussianwalker_8way.png")

    walk.step()
    walk.draw()

    # clock.tick(10)
    pygame.display.update()
