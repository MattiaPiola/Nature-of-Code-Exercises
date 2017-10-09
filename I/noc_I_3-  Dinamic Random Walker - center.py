from random import randint, random

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("A random walker trying to get back to the center of the screen.")
still_on = True
clock = pygame.time.Clock()
walk_is_here = False

class Walker():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1

    def draw(self):
        pygame.draw.line(display,(255,255,255),(self.x, self.y),(self.x, self.y))

    def step(self):
        step_x = random()
        relative_x = self.x/display.get_width()
        left_p = 0.66*relative_x
        right_p = 0.33 + left_p
        if step_x <= left_p:
            self.x -= 1
        elif step_x >= right_p:
            self.x += 1
        else:
            pass

        step_y = random()
        relative_y = self.y / display.get_height()
        up_p = 0.66 * relative_y
        down_p = 0.33 + up_p
        if step_y <= up_p:
            self.y -= 1
        elif step_y >= down_p:
            self.y += 1
        else:
            pass

while still_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            display.fill((0, 0, 0))
            walk = Walker(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            relative_x = pygame.mouse.get_pos()[0] / display.get_width()
            relative_y = pygame.mouse.get_pos()[1] / display.get_height()
            print(relative_x, relative_y)
            walk_is_here = True

    if walk_is_here:
        walk.step()
        walk.draw()
    pygame.display.update()
