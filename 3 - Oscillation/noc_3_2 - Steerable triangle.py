import pygame
import numpy as np

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()

class Rotator():
    def __init__(self):
        # dinamics
        self.pos = np.array([400,300], dtype="float64")
        self.vel = np.array([0,0], dtype="float64")
        self.max_vel = 10
        self.acceleration = np.array([0, 0], dtype="float64")
        self.max_acceleration = 1
        self.angle = 0
        self.max_turn_angle = np.pi/2

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
        acc_vector = np.divide(acc_vector, np.linalg.norm(self.max_acceleration))
        return acc_vector

    def get_turn_vector(self, direction):
        turn_angle = self.angle + self.max_turn_angle*direction
        turn_vector = np.array([np.cos(turn_angle), np.sin(turn_angle)])
        turn_vector = np.divide(turn_vector, np.linalg.norm(self.max_acceleration))
        return turn_vector

    def draw(self):
        self.shape = np.array([np.add(self.pos, [self.size * np.cos(self.angle), self.size * np.sin(self.angle)]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 2 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 2 / 3))]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 4 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 4 / 3))])],
                              dtype="int32")
        pygame.draw.polygon(display, (0, 255, 0), self.shape, 0)

    def update(self):
        self.vel += self.acceleration
        vel_mag = np.linalg.norm(self.vel)
        if vel_mag != 0 and vel_mag > self.max_vel:
            self.vel = np.divide(self.vel, vel_mag)*self.max_vel
        self.pos += self.vel
        self.angle = np.arctan2(self.vel[1],self.vel[0])
        if self.angle > np.pi*2:
            self.angle -= np.pi*2
        rotator.acceleration *= 0

rotator = Rotator()
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
            elif event.key == pygame.K_UP:
                accelerating = "acc"
            elif event.key == pygame.K_DOWN:
                accelerating = "brake"
        if event.type == pygame.KEYUP:
            turning = False
            accelerating = False

    if turning == "left":
        force = rotator.get_turn_vector(-1)
        rotator.apply_force(force)
    elif turning == "right":
        force = rotator.get_turn_vector(+1)
        rotator.apply_force(force)
    if accelerating == "acc":
        force = rotator.get_acc_vector()
        rotator.apply_force(force)
    elif accelerating == "brake":
        force = rotator.get_acc_vector()
        if np.linalg.norm(rotator.vel) > np.linalg.norm(force):
            rotator.apply_force(-force)
        else:
            rotator.vel *= 0.00001

    rotator.update()
    rotator.draw()

    clock.tick(30)
    pygame.display.update()
