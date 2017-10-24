import pygame
import numpy as np

pygame.init()
disp_sizes = (800,600)
display = pygame.display.set_mode(disp_sizes)
pygame.display.set_caption("PYGAME")
still_on = True
clock = pygame.time.Clock()


class Weight():
    def __init__(self, x):
        self.pos = np.array([x, 300])
        self.phase = np.random.randint(0,100,1)
        self.period = np.random.randint(500,5000,1)
        self.amplitude = np.random.randint(50, 300, 1)


    def update(self):
        move = self.amplitude * np.sin(np.pi*2*(pygame.time.get_ticks()+self.phase)/self.period)
        self.pos[1] = 300 + move


    def draw(self):
        pygame.draw.circle(display, (255,0,0), self.pos.astype("int32"), 25)
        pygame.draw.line(display, (255,255,255),[self.pos[0], 0], self.pos+[0,-25])

objs = []

w1 = Weight(100)
w2 = Weight(300)
w3 = Weight(500)
w4 = Weight(700)
objs.append(w1)
objs.append(w2)
objs.append(w3)
objs.append(w4)

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
