import sys

import pygame

# init
pygame.init()
screen = pygame.display.set_mode((800, 400))  # w, h
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()

test_font = pygame.font.FontType("font/Pixeltype.ttf", 50)  # font_type, font_size

# surface
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My Game", True, "Black")  # text, antialias?, color

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
# rectangle
player_rect = player_surface.get_rect(midbottom=(80, 300))

# main game logic
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 100))

    snail_rect.x -= 4

    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)
