from random import random

import pygame
import numpy as np

pygame.init()
disp_sizes = (1000,700)
display = pygame.display.set_mode(disp_sizes)
pygame.display.set_caption("PYGAME")
still_on = True
clock = pygame.time.Clock()
objs = []


class Leg():
    def __init__(self, joint, phase, front= True):
        if front:
            self.joint = joint
            self.color = (0,200,0)
            self.start_angle = np.pi * phase
        else:
            self.joint = joint + [70,-70]
            self.color = (50, 100, 0)
            self.start_angle = np.pi * (phase + 1)
        self.leg_len = 150
        self.knee = np.subtract(self.joint, (0, self.leg_len))
        self.foot = np.subtract(self.joint, (0, -1.5*self.leg_len))
        self.velocity = np.array([0.2, 0.2])
        self.angle = np.array([self.start_angle, self.start_angle - np.pi/2])
        self.amplitude = np.array([25, 5])

        self.move = []

    def update(self):
        self.angle += self.velocity
        self.move = np.array(np.multiply(self.amplitude, np.cos(self.angle)))

    def draw(self):
        pygame.draw.lines(display, self.color, False, (self.joint, self.knee+self.move, self.foot+self.move*2), 10)



class Insect():
    def __init__(self):
        self.pos = np.array((200,200))
        self.leg_joints = np.empty((2))
        for i in range(3):
            joint = np.array([self.pos +((i+1)*500/4, 100)])
            self.leg_joints = np.vstack((self.leg_joints, joint))
        self.leg_joints = self.leg_joints[1:]

        self.back_legs = []
        for j in range(len(self.leg_joints)):
            leg = Leg(self.leg_joints[j], j, False)
            self.back_legs.append(leg)

        self.front_legs = []
        for j in range(len(self.leg_joints)):
            leg = Leg(self.leg_joints[j], j)
            self.front_legs.append(leg)


    def update(self):
        for leg in self.front_legs:
            leg.update()

        for leg in self.back_legs:
            leg.update()

    def draw(self):
        for leg in self.back_legs:
            leg.draw()
        pygame.draw.circle(display, (160,240,0), (self.pos + (500,100)),100)
        pygame.draw.circle(display, (140,140,0), (self.pos + (550,55)),20)
        pygame.draw.circle(display, (100,100,0), (self.pos + (560,50)),10)
        pygame.draw.circle(display, (0, 255, 0), (self.pos + (0, 100)), 100)
        pygame.draw.circle(display, (0, 240, 0), (self.pos + (-75, 75)), 75)
        pygame.draw.circle(display, (0, 225, 0), (self.pos + (-100, 0)), 50)
        pygame.draw.rect(display, (0,255,0),(self.pos, (500,200)))
        for leg in self.front_legs:
            leg.draw()


ins = Insect()
objs.append(ins)

while still_on:
    display.fill((100,150,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")

    for obj in objs:
        obj.update()
        obj.draw()
    clock.tick(60)
    pygame.display.update()
