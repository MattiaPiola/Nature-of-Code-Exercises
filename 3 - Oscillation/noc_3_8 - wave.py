import pygame
import numpy as np
from noise._perlin import noise1

pygame.init()
disp_sizes = (800,600)
display = pygame.display.set_mode(disp_sizes)
pygame.display.set_caption("PYGAME")
still_on = True
clock = pygame.time.Clock()

num = 70
sea_drops = 10
spacing = disp_sizes[0]/num
amp = 70
ang_vel = 0.02
color = (0, 0, 255)
period = 60


class Ball():
    def __init__(self, x, y):
        self.x = x
        self.start_y = y
        self.y = y
        self.size = disp_sizes[0] / (1.5*num)
        self.angle = x/period
        self.time = np.random.randint(0, 100)

    def update(self):
        self.y = self.start_y + amp * (np.sin(self.angle)) + noise1(np.sin(self.angle+self.time))*np.log(1/self.y)
        self.angle += ang_vel
        self.time += 0.025

    def draw(self):
        wave_spacing = (disp_sizes[1] - self.y) / sea_drops
        for i in range(sea_drops):
            pygame.draw.circle(display, (0, 0, 155), (int(self.x), int(self.y+wave_spacing*i+1)), int(self.size))
        pygame.draw.circle(display, color, (int(self.x), int(self.y)), int(self.size))


wave = []

for i in range(num+1):
    b_x = spacing * (i)
    ball = Ball(b_x, disp_sizes[1]/2)
    wave.append(ball)

while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")

    for ball in wave:
        ball.update()
        ball.draw()

    clock.tick(60)
    pygame.display.update()
