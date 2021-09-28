import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("8085 Simulator")
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

while True:
    screen.fill((0, 0, 80))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()