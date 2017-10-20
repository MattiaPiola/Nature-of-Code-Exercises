from random import randint

import pygame
import numpy as np


pygame.init()
display = pygame.display.set_mode((3000, 1400))
still_on = True
clock = pygame.time.Clock()

class Sun():
    def __init__(self):
        self.pos = np.array([display.get_width()/2, display.get_height()/2], dtype="float32")
        self.velocity = np.array([0,0], dtype="float32")
        self.acceleration = np.zeros(2, dtype="float32")
        self.mass = 70000.0
        self.size = 100

    def apply_force(self, force):
        self.acceleration += (force / self.mass).astype("float32")

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = 0.0

    def draw(self):
        pygame.draw.circle(display, (255,255,0), self.pos, self.size)


class Planet():
    def __init__(self, pos, mass):
        self.pos  = np.array(pos, dtype="float32")
        self.velocity = np.array([randint(0,0), randint(5,15)], dtype="float32")
        self.acceleration = np.zeros(2, dtype="float32")
        self.mass = mass
        self.size = int(np.floor(self.mass/4))
        self.color = (randint(50,205), randint(50,255), randint(50,255))
        self.outer_color = np.subtract(self.color, (50, 50, 50))

    def apply_force(self, force):
        self.acceleration += (force/self.mass).astype("float32")

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = 0.0


    def draw(self):
        pygame.draw.circle(display, self.color, self.pos, self.size)
        pygame.draw.circle(display, self.outer_color, self.pos, self.size, 3)


def grav_attraction(obj1, obj2):
    force_dir = obj2.pos - obj1.pos
    distance = np.linalg.norm(force_dir)
    distance.clip(10)
    force_mag = (obj1.mass * obj2.mass)/(distance**2)
    force = np.multiply(np.divide(force_dir, distance),force_mag)
    obj1.apply_force(force)
    obj2.apply_force(-force)

planets = []
sun = Sun()


while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONUP:
            planet = Planet(pygame.mouse.get_pos(), randint(50,200))
            planets.append(planet)
            # pygame.image.save(display, "screenshot.png")

    for i in range(len(planets)):
        for x in range(len(planets)):
            if i != x:
                grav_attraction(planets[i], planets[x])

    for planet in planets:
        grav_attraction(planet,sun)
        planet.update()
        distance = np.linalg.norm(np.subtract(sun.pos, planet.pos))
        if np.linalg.norm(planet.pos) > 100000 or distance < sun.size:
            planets.remove(planet)
        else:
            planet.draw()
    # sun.update()
    sun.draw()

    # clock.tick(60)
    pygame.display.update()
