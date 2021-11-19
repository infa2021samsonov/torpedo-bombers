import pygame
from gameplay import *
from pygame.gfxdraw import *
import Menu
from gameplay import *
from ModelShip import *

pygame.init()
# еще возможно  'gameplay'
screen_type = 'menu'
# цвет моря
sea_color = (62, 145, 179)

FPS = 60
screen = pygame.display.set_mode((1600, 900))
screen.fill(sea_color)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

# это тоже код для проверки
ship = GameShip(1000, 0.01, 450, 800, 0, 10, 100, (1, 1, 1), 100, 10, 0.1)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if screen_type == 'menu':
                # код Андрея для отрисовки меню и работы с кнопкой Play
                print('menu')

            if screen_type == 'gameplay':
                # Код Сома для отрисовки геймплея
                print('gameplay')

            # код Вовы для проверки - можно стирать
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_w]:
                print("ffw")
                ship.MoveForward(pi, screen)
    pygame.display.update()
pygame.quit()
