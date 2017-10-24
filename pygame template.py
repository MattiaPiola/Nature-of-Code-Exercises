import pygame

pygame.init()
disp_sizes = (800,600)
display = pygame.display.set_mode(disp_sizes)
pygame.display.set_caption("PYGAME")
still_on = True
clock = pygame.time.Clock()


while still_on:
    # display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_on = False
        # if event.type == pygame.MOUSEBUTTONUP:
            # pygame.image.save(display, "screenshot.png")


    clock.tick(60)
    pygame.display.update()
