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
        self.angle = 0
        self.angular_vel = 0
        self.angular_acc = 0



        # appearance
        self.size = 50
        self.shape = np.array([np.add(self.pos, [self.size * np.cos(self.angle), self.size * np.sin(self.angle)]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 2 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 2 / 3))]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 4 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 4 / 3))])],
                              dtype="int32")

    def draw(self):
        self.shape = np.array([np.add(self.pos, [self.size * np.cos(self.angle), self.size * np.sin(self.angle)]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 2 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 2 / 3))]),
                               np.add(self.pos, [self.size / 3 * np.cos(self.angle + (np.pi * 4 / 3)),
                                                 self.size / 3 * np.sin(self.angle + (np.pi * 4 / 3))])],
                              dtype="int32")
        pygame.draw.polygon(display, (0, 255, 0), self.shape, 0)

    def update(self):
        self.angular_vel += self.angular_acc
        self.angle += self.angular_vel
        if self.angle > np.pi*2:
            self.angle -= np.pi*2


rotator = Rotator()


while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
            # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotator.angular_acc = -0.1
                print(rotator.angular_vel)
            elif event.key == pygame.K_RIGHT:
                rotator.angular_acc = +0.1
                print(rotator.angular_vel)
        if event.type == pygame.KEYUP:
            rotator.angular_acc = 0
            print(rotator.angular_vel)

    rotator.update()
    rotator.draw()

    clock.tick(10)
    pygame.display.update()
