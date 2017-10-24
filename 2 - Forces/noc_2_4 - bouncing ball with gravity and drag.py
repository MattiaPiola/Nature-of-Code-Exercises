from random import randint

import pygame
import numpy as np

pygame.init()
displ_sizes = [1000,1300]
display = pygame.display.set_mode(displ_sizes)
still_on = True
clock = pygame.time.Clock()

friction_zone = np.array([500,1500])

class Ball():

    def __init__(self, x = display.get_width()/2, y = display.get_height()/2, velocity = [10,0], mass = 1):
        # Movement
        self.pos = np.array([x,y],dtype="float32")
        self.velocity = np.array(velocity, dtype="float32")
        self.acceleration = np.zeros(2, dtype="float32")
        self.mass = mass

        # Appearance
        self.outer_col = [randint(0, 205), randint(0, 205), randint(0, 205)]
        self.inner_col = np.add(self.outer_col, [50, 50, 50])
        self.size = int(np.floor(self.mass/100))
        self.accel_arrow = self.acceleration

    def update(self):
        self.velocity += self.acceleration
        self.accel_arrow = self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0

    def apply_force(self, force):
        self.acceleration += (force/self.mass).astype("float32")

    def check_boundaries(self):
        for i in range(2):
            if self.pos[i] < 0 or self.pos[i] > displ_sizes[i]:
                new_force=np.array([0,0], dtype="int32")
                new_force[i] = -2*self.velocity[i]*self.mass
                self.apply_force(new_force)
                if i == 1:
                    self.apply_force(-gravity*self.mass)

    def check_zone(self):
        if self.pos[1] > friction_zone[0] and self.pos[1] < friction_zone[1]:
            return True
        else:
            return False

    def drag(self):
        drag_mag = -(np.linalg.norm(self.velocity)) ** 2 * 50 #* self.size
        drag_dir = np.divide(ball.velocity, np.linalg.norm(self.velocity))
        drag = drag_dir * drag_mag
        drag = drag.clip(max=5, out = drag)
        self.apply_force(drag)

    def draw(self):
        pygame.draw.circle(display, (self.inner_col), self.pos, self.size)
        pygame.draw.circle(display, (self.outer_col), self.pos, self.size, 3)
        pygame.draw.line(display, (0,255,0),self.pos, self.pos+self.velocity*2,4)
        pygame.draw.line(display, (255, 255, 0), self.pos, self.pos + self.accel_arrow*2, 4)

balls = []

gravity = np.array([0,10], dtype="int32")

while still_on:
    display.fill((0,0,0))
    pygame.draw.rect(display, (50, 50, 50, 0.1), (0, friction_zone[0], displ_sizes[0], friction_zone[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            ball = Ball(x = pygame.mouse.get_pos()[0], y = pygame.mouse.get_pos()[1], mass = randint(5000,12500),
                        velocity=[0,0])
            balls.append(ball)
            # pygame.image.save(display, "screenshot.png")
        if event.type == pygame.KEYDOWN:
            spawn_balls()

    for ball in balls:
        ball.apply_force(gravity*ball.mass)
        ball.check_boundaries()

        if ball.check_zone() and np.linalg.norm(ball.velocity) != 0 and ball.pos[1] > 3:
            ball.drag()

        ball.update()
        ball.draw()

    clock.tick(30)
    pygame.display.update()
