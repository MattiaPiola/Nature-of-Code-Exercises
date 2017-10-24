import pygame
import numpy as np

pygame.init()
disp_sizes = (800,600)
display = pygame.display.set_mode(disp_sizes)
still_on = True
clock = pygame.time.Clock()

class Spaceship():
    def __init__(self):
        # dinamics
        self.pos = np.array([400,300], dtype="float64")
        self.vel = np.array([0,0], dtype="float64")
        self.max_vel = 10
        self.acceleration = np.array([0, 0], dtype="float64")
        self.max_acceleration = 1
        self.angle = 0

        # appearance
        self.size = 10
        self.shape = np.array([np.add(self.pos, [self.size * np.cos(self.angle), self.size * np.sin(self.angle)]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 2 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 2 / 3))]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 4 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 4 / 3))])],
                              dtype="int32")


    def apply_force(self, force):
        self.acceleration += force

    def get_acc_vector(self):
        acc_vector = np.array([np.cos(self.angle), np.sin(self.angle)])
        acc_vector = np.multiply(acc_vector,self.max_acceleration)
        return acc_vector

    def draw(self):
        self.shape = np.array([np.add(self.pos, [self.size * np.cos(self.angle), self.size * np.sin(self.angle)]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 2 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 2 / 3))]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 4 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 4 / 3))])],
                              dtype="int32")
        pygame.draw.polygon(display, (0, 255, 0), self.shape, 0)

    def check_boundaries(self):
        for i in range(2):
            if self.pos[i] > disp_sizes[i]:
                self.pos[i] = 0
            if self.pos[i] < 0:
                self.pos[i] = disp_sizes[i]


    def update(self):
        self.vel += self.acceleration
        self.pos += self.vel
        if self.angle > np.pi*2:
            self.angle -= np.pi*2
        spaceship.acceleration *= 0


spaceship = Spaceship()
turning = False
accelerating = False

while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
            # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turning = "left"
            elif event.key == pygame.K_RIGHT:
                turning = "right"
            if event.key == pygame.K_z:
                accelerating = True

        if event.type == pygame.KEYUP:
            turning = False
            accelerating = False

    if turning == "left":
        spaceship.angle -= np.pi/10
    elif turning == "right":
        spaceship.angle += np.pi / 10

    if accelerating:
        force = spaceship.get_acc_vector()
        spaceship.apply_force(force)

    spaceship.update()
    spaceship.check_boundaries()
    spaceship.draw()

    clock.tick(30)
    pygame.display.update()
