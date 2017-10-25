import pygame
import numpy as np

pygame.init()
disp_sizes = (800,600)
display = pygame.display.set_mode(disp_sizes)
pygame.display.set_caption("PYGAME")
still_on = True
clock = pygame.time.Clock()

gravity = 0.4
fulcrum_0 = np.array([400, 0])

class Pendulum():
    def __init__(self, x):
        self.r = 500
        self.angle = 0
        self.ang_vel = 0.01
        self.ang_acc = 0
        self.origin = fulcrum_0
        self.pos = np.array([self.r*np.sin(self.angle),self.r*np.cos(self.angle)])+self.origin

    def update(self):
        self.ang_acc = (-1 * gravity/self.r) * np.sin(self.angle)
        self.ang_vel += self.ang_acc
        self.angle += self.ang_vel
        self.pos = np.array([self.r * np.sin(self.angle), self.r * np.cos(self.angle)]) + self.origin

    def draw(self):
        pygame.draw.line(display, (255, 255,255), fulcrum_0, self.pos)
        pygame.draw.circle(display, (100,0,0), self.pos.astype("int32"), 25)

def get_tension(obj, fulcrum):
    tension = obj.pos - fulcrum
    tension = np.divide(tension, np.linalg.norm(tension)).astype("int")
    return tension


objs = []

p1 = Pendulum(400)

objs.append(p1)

while still_on:
    display.fill((0,0,0))
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
