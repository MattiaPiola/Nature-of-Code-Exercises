import pygame
from math import floor
from noise.perlin import SimplexNoise

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()

noise = SimplexNoise()

class Walker():

    def __init__(self):
        self.x = display.get_width()/2
        self.y = display.get_height()/2
        self.x_off = 10001
        self.y_off = 10000
        self.rate = 0.001
        self.speed = 1
        self.radius = 20

    def draw(self):
        color = lambda x : int(floor(abs(noise.noise2(self.x+x,self.y+x)*255)))
        pygame.draw.circle(display,(color(1),color(1),255),(int(floor(self.x)), int(floor(self.y))),self.radius)

    def step(self):
        step_x = noise.noise2(self.x_off,self.x_off)*self.speed
        step_y = noise.noise2(self.y_off,self.y_off)*self.speed
        self.x += step_x
        self.y += step_y
        self.x_off += self.rate
        self.y_off += self.rate

    def change_size(self):
        self.radius = floor(abs(noise.noise2(self.x_off,self.y_off)*2))

walker = Walker()

while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.image.save(display, "screenshot.png")

    walker.step()
    walker.change_size()
    walker.draw()

    # clock.tick(10)
    pygame.display.update()
