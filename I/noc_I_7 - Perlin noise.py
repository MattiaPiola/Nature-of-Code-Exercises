import pygame
from math import floor
from noise.perlin import SimplexNoise

pygame.init()
display = pygame.display.set_mode((200,100))
still_on = True
clock = pygame.time.Clock()

noise = SimplexNoise()
noise_rate = 0.01

def draw(x,y):
    color = int(floor((noise.noise2(x*noise_rate,y*noise_rate)+1)*125))
    pygame.draw.line(display,(color, color, color), (x, y), (x, y))

def draw_all():
    for x in range(display.get_width()):
        for y in range(display.get_height()):
            draw(x, y)

            
while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:

    draw_all()

    clock.tick(10)
    pygame.display.update()
