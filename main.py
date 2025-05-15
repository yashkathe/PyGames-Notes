import sys

import pygame

# init
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()

# main game logic
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # draw our elements and update everything
    pygame.display.update()
    clock.tick(60)
