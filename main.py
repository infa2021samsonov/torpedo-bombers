import pygame
from gameplay import *
from pygame.draw import *
pygame.init()
screen_type = 'menu'
sea_color = (63, 145, 179)
FPS = 30
screen = pygame.display.set_mode((1600, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_type == 'menu':
                print("Андрей")

            if screen_type == 'gameplay':

                print("Сом")

pygame.quit()