from random import randint

import pygame
import numpy as np

pygame.init()
displ_sizes = [800,600]
display = pygame.display.set_mode(displ_sizes)
still_on = True
clock = pygame.time.Clock()

class Spring:
    def __init__(self):
        self.k = 0.1
        self.rest_length = 200
        self.pos = [displ_sizes[0]/2, 0]
        self.width = 1

    def get_spring_tension(self, ball):
        diff_vector = ball.pos - self.pos
        curr_length = np.linalg.norm(diff_vector)
        diff_vector = np.divide(diff_vector, curr_length)
        delta_length = curr_length - self.rest_length
        self.width = 1000/delta_length
        tension = -1 * diff_vector * delta_length
        return tension

    def draw(self, ball):
        pygame.draw.line(display, (255, 255, 255), self.pos, ball.pos, int(self.width))

class Ball():
    def __init__(self, x = display.get_width()/2, y = display.get_height()/2, velocity = [10,0], mass = 1):
        # Movement
        self.pos = np.array([x,y],dtype="int32")
        self.velocity = np.array(velocity, dtype="int32")
        self.acceleration = np.zeros(2, dtype="int32")
        self.mass = mass

        # Appearance
        self.outer_col = [randint(0, 205), randint(0, 205), randint(0, 205)]
        self.inner_col = np.add(self.outer_col, [50, 50, 50])
        self.size = self.mass*5

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0

    def apply_force(self, force):
        self.acceleration += (force/self.mass).astype("int32")

    def draw(self):
        pygame.draw.circle(display, (self.inner_col), self.pos, self.size)
        pygame.draw.circle(display, (self.outer_col), self.pos, self.size, 3)

balls = []
spring = Spring()

gravity = np.array([0,5], dtype="int32")

while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            balls = []
            ball = Ball(x = pygame.mouse.get_pos()[0], y = pygame.mouse.get_pos()[1], velocity = [0, 0],
                        mass = randint(15,25))
            balls.append(ball)
            spring = Spring()

            # pygame.image.save(display, "screenshot.png")
        if event.type == pygame.KEYUP:
            for ball in balls:
                wind = np.array([-20,0], dtype="int32")
                ball.apply_force(wind)

    for ball in balls:
        ball.apply_force(gravity*ball.mass)
        tension = spring.get_spring_tension(ball)
        ball.apply_force(tension)
        ball.apply_force(gravity*ball.mass)
        ball.update()
        spring.draw(ball)
        ball.draw()


    clock.tick(60)
    pygame.display.update()


