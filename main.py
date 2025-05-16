import sys

import pygame

# init
pygame.init()
screen = pygame.display.set_mode((800, 400))  # w, h
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()

test_font = pygame.font.FontType("font/Pixeltype.ttf", 50)  # font_type, font_size

# surface
sky_surface = pygame.image.load("graphics/sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("My Game", True, "Black")  # text, antialias?, color

# main game logic
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 100))

    pygame.display.update()
    clock.tick(60)
