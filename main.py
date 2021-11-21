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

# Это над для создания класса геймплея - не трогать и не смотреть
Left_player = GameShip(100,1,1,1,0,10,10, (0,0,0),10,10,0.01, 4, 10*60, 100)
Right_player = GameShip(100,1,1,1,0,10,10, (0,0,0),10,10,0.01, 4, 20*60, 100)

# создание классов игровых экранов - меню и и геймплея
gameplay_screen = Gameplay(Left_player, Right_player)
# Экран меню Андрея


while not finished:
    # для отрисовки интерфейса
    if screen_type == 'menu':
        gameplay_screen.time = 0

    if screen_type == 'gameplay':
        gameplay_screen.time -= 1
        gameplay_screen.drawShips(screen)
        gameplay_screen.drawTorpeds(screen)
        gameplay_screen.drawTime(screen)
        gameplay_screen.drawInfo(screen)
        gameplay_screen.drawTorpedIndicators(screen, gameplay_screen.leftPl, 'left')
        gameplay_screen.drawTorpedIndicators(screen, gameplay_screen.rightPl, 'right')
        gameplay_screen.drawXP(screen, gameplay_screen.leftPl, 'left')
        gameplay_screen.drawXP(screen, gameplay_screen.rightPl, 'right')

    clock.tick(FPS)
    pygame.display.update()
    screen.fill(sea_color)

    # для обработкинажатий кнопок с клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if screen_type == 'menu':
                # просто код чтобы тестировать - можно стереть
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    screen_type = 'gameplay'
                    gameplay_screen.time = 300*FPS

            if screen_type == 'gameplay':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    """ добавление тяги у gameplay_screen.leftPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    """ убавление тяги у gameplay_screen.leftPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    """ правее gameplay_screen.leftPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    """ левее gameplay_screen.leftPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    """добавление тяги у gameplay_screen.righPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                    """ убавление тяги у gameplay_screen.righPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    """ правее gameplay_screen.righPl"""
                if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                    """ левее gameplay_screen.righPl"""

pygame.quit()
