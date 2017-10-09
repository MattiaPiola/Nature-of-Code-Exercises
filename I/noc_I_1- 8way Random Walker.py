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
        step_x = randint(-1, 1)*self.speed
        step_y = randint(-1, 1)*self.speed
        self.x += step_x
        self.y += step_y



walk = Walker()

walk.draw()


while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "randomwalker_8way.png")

    walk.step()
    walk.draw()
    pygame.display.update()
