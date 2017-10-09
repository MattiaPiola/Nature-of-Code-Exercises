import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
still_on = True
clock = pygame.time.Clock()

while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False

    clock.tick(60)
    pygame.display.update()
