import pygame
from gameplay import *
from pygame.gfxdraw import *
import Menu
from gameplay import *

pygame.init()
screen_type = 'menu'
sea_color = (62, 145, 179)
FPS = 30
screen = pygame.display.set_mode((1600, 900))


screen.fill(sea_color)

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
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_w]:
                ModelShip.MoveForward()
            if screen_type == 'gameplay':

                print("Сом")

pygame.quit()