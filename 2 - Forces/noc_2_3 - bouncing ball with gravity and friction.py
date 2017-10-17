from random import randint

import pygame
import numpy as np

pygame.init()
displ_sizes = [2000,600]
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
        self.size = self.mass*5

    def update(self):
        self.velocity += self.acceleration
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
        if self.pos[0] > friction_zone[0] and self.pos[0] < friction_zone[1]:
            return True
        else:
            return False

    def draw(self):
        pygame.draw.circle(display, (self.inner_col), self.pos, self.size)
        pygame.draw.circle(display, (self.outer_col), self.pos, self.size, 3)

balls = []

gravity = np.array([0,2], dtype="int32")

while still_on:
    display.fill((0,0,0))
    pygame.draw.rect(display, (255,0,0,50),(friction_zone[0],0,friction_zone[1],displ_sizes[1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            ball = Ball(x = pygame.mouse.get_pos()[0], y = pygame.mouse.get_pos()[1], mass = randint(2,60),
                        velocity=[randint(1,10),0])
            balls.append(ball)
            # pygame.image.save(display, "screenshot.png")
        if event.type == pygame.KEYUP:
            for ball in balls:
                wind = np.array([-20,0], dtype="int32")
                ball.apply_force(wind)

    for ball in balls:
        ball.check_boundaries()
        ball.update()
        if ball.check_zone() and np.linalg.norm(ball.velocity) > 0 and ball.pos[1] > 3:
                friction_mag = -2 * 1
                friction_dir = np.divide(ball.velocity, np.linalg.norm(ball.velocity))
                friction = friction_dir * friction_mag
                ball.apply_force(friction)
                print(np.linalg.norm(ball.velocity))

        ball.draw()
        ball.apply_force(gravity*ball.mass)


    # clock.tick(60)
    pygame.display.update()


