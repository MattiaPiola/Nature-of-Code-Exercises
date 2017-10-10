from random import randint, gauss, random, randrange, uniform

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
still_on = True
clock = pygame.time.Clock()

def montecarlo():
    num = uniform(-1, 1)
    p_num = abs(num)**2
    chance = random()
    if chance < p_num:
        return num
    else:
        return 0.0


class Walker():

    def __init__(self):
        self.x = display.get_width()/2
        self.y = display.get_height()/2
        self.past_x = self.x
        self.past_y = self.y
        self.speed = 20

    def draw(self):
        color = randint(255,255)
        pygame.draw.line(display,(color,color,color),(self.past_x, self.past_y),(self.x, self.y))

    def step(self):
        step_x = montecarlo()*self.speed
        step_y = montecarlo()*self.speed
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
            pygame.image.save(display, "montecarlowalker_8way.png")

    walk.step()
    walk.draw()

    clock.tick(30)
    pygame.display.update()
