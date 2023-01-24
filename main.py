import pygame
import sys

pygame.init()

window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # dsadfs dgad
    pygame.display.update()