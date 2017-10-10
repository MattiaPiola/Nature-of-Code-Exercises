import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 10
        self.y_speed = 12

    def update_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def check_boundaries(self):
        if self.x < 0 or self.x > display.get_width():
            self.x_speed *= -1
        if self.y < 0 or self.y > display.get_height():
            self.y_speed *= -1

    def draw(self):
        pygame.draw.circle(display, (255,255,255), (self.x, self.y), 20)



ball = Ball(400, 200)


while still_on:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")

    ball.update_pos()
    ball.check_boundaries()
    ball.draw()


    clock.tick(60)
    pygame.display.update()
