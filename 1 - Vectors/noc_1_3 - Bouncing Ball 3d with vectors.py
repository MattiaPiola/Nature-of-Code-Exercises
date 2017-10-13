import pygame
import numpy as np

pygame.init()
display = pygame.display.set_mode((1000, 1000))
still_on = True
clock = pygame.time.Clock()
white = (255, 255, 255)


class Box():
    def __init__(self):
        self.sizes = np.array([500,500,400])
        # cube vertices
        self.center = np.array([(display.get_width()-self.sizes[0]+self.sizes[2]/4)/2, (display.get_height()+self.sizes[1])/2-self.sizes[2]/4])
        self.base_1 = self.center + np.array([self.sizes[0], 0])
        self.base_2 = self.base_1 - np.array([self.sizes[2] / 2, -self.sizes[2] / 2])
        self.base_3 = self.center - np.array([self.sizes[2] / 2, -self.sizes[2] / 2])
        self.top_center = self.center - np.array([0, self.sizes[1]])
        self.top_1 = self.base_1 - np.array([0, self.sizes[1]])
        self.top_2 = self.base_2 - np.array([0, self.sizes[1]])
        self.top_3 = self.base_3 - np.array([0, self.sizes[1]])

        self.hits_back = []
        self.hits_front = []

    def draw_back(self):
        #draw lines
        pygame.draw.line(display, white, self.center, self.base_1, 3)
        pygame.draw.line(display, white, self.center, self.top_center, 3)
        pygame.draw.line(display, white, self.base_3, self.center, 3)

        for hit in self.hits_back:
            wall = hit[2]
            color = [0,0,0]
            color[wall] = 255
            pygame.draw.circle(display, color, hit[0:2], 3)

    def draw_front(self):
        # cube base
        pygame.draw.line(display, white, self.base_1, self.base_2, 3)
        pygame.draw.line(display, white, self.base_2, self.base_3, 3)
        # cube sides
        pygame.draw.line(display, white, self.base_1, self.top_1, 3)
        pygame.draw.line(display, white, self.base_2, self.top_2, 3)
        pygame.draw.line(display, white, self.base_3, self.top_3, 3)
        # cube top
        pygame.draw.line(display, white, self.top_center, self.top_1, 3)
        pygame.draw.line(display, white, self.top_1, self.top_2, 3)
        pygame.draw.line(display, white, self.top_2, self.top_3, 3)
        pygame.draw.line(display, white, self.top_3, self.top_center, 3)

        for hit in self.hits_front:
            wall = hit[2]
            color = [0,0,0]
            selector = [1,2,0]
            color[wall] = 255
            color[selector[wall]] = 255
            pygame.draw.circle(display, color, hit[0:2], 3)


class Ball():
    def __init__(self, container):
        self.size = 25
        self.pos = np.array([self.size, self.size, self.size])
        self.velocity = np.random.random_integers(0, 10, 3)
        self.container = container
        self.hits_back = []
        self.hits_front = []

    def update_pos(self):
        self.pos += self.velocity

    def random_vel(self):
        self.velocity = np.random.random_integers(0, 10, 3)

    def check_boundaries(self):
        for i in range(3):
            if self.pos[i] < 0 + self.size:
                self.velocity[i] *= -1
                hit = self.get_asson_pos()
                wall = [i]
                hit = np.concatenate((hit,wall))
                if i == 0:
                    self.container.hits_back.append(hit)
                else:
                    self.container.hits_front.append(hit)
            elif self.pos[i] > self.container.sizes[i]-self.size:
                self.velocity[i] *= -1
                hit = self.get_asson_pos()
                wall = [i]
                hit = np.concatenate((hit, wall))
                if i == 0:
                    self.container.hits_front.append(hit)
                else:
                    self.container.hits_back.append(hit)

    def get_size(self):
        size = int(np.ceil(self.size/3+(2*self.size/3)*((self.container.sizes[2]-self.pos[2])/self.container.sizes[2])))
        return size

    def get_color(self):
        red = int(np.ceil(120+135*((self.container.sizes[2]-self.pos[2])/self.container.sizes[2])))
        color = (red, 0, 0)
        return color

    def get_asson_pos(self):
        x_asson_pos = np.array([self.pos[0],0])
        y_asson_pos = np.array([0, self.pos[1]])
        z_asson_pos = np.array([self.pos[2]/2, -self.pos[2]/2])
        asson_pos = x_asson_pos + y_asson_pos + z_asson_pos + self.container.top_3
        asson_pos = asson_pos.astype("int")
        return asson_pos

    def draw(self):
        pygame.draw.circle(display, self.get_color(), self.get_asson_pos(), self.get_size())
        pygame.draw.line(display, (255, 255, 0), self.get_asson_pos(), (self.get_asson_pos()+(self.velocity[0]*2 + self.velocity[2], self.velocity[1]*2 - self.velocity[2])), 3)


box = Box()
ball = Ball(box)


while still_on:
    display.fill((0, 0, 0))
    box.draw_back()
    ball.update_pos()
    ball.check_boundaries()
    ball.draw()
    box.draw_front()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.random_vel()



            # pygame.image.save(display, "screenshot.png")

    clock.tick(30)
    pygame.display.update()
