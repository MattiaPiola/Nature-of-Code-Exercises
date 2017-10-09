from random import randint, random

import pygame

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("A random walker following your mouse.")
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
        mouse_x = pygame.mouse.get_pos()[0]
        x_mouse_dist = mouse_x - self.x
        relative_x = x_mouse_dist/display.get_width()
        left_p = 0.33 - relative_x * 0.33
        right_p = 0.33+left_p
        step_x = random()
        if step_x <= left_p:
            self.x -= 1
        elif step_x >= right_p:
            self.x += 1

        mouse_y = pygame.mouse.get_pos()[1]
        y_mouse_dist = mouse_y - self.y
        relative_y = y_mouse_dist / display.get_height()
        up_p = 0.33 - relative_y * 0.33
        down_p = 0.33 + up_p
        step_y = random()
        if step_y <= up_p:
            self.y -= 1
        elif step_y >= down_p:
            self.y += 1


walk = Walker()

walk.draw()


while still_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False

    walk.step()
    walk.draw()
    #clock.tick(60)
    pygame.display.update()
