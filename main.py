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
DISPLAY_W = 1500
DISPLAY_H = 800
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
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
        Menu.Mainmenu().blit_screen()
        Menu.Mainmenu().display_menutext(screen)
        Menu.Choose_Ship_pl1(screen).display_menu(screen)
        Menu.Choose_Ship_pl2(screen).display_menu(screen)



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
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            Menu.Mainmenu().START_KEY = True
                        if event.key == pygame.K_BACKSPACE:
                            Menu.Mainmenu().BACK_KEY = True
                        if event.key == pygame.K_s:
                            Menu.Mainmenu().DOWN_KEY1 = True
                            Menu.Choose_Ship_pl1(screen).move_cursor()
                        if event.key == pygame.K_k:
                            Menu.Mainmenu().DOWN_KEY2 = True
                            Menu.Choose_Ship_pl2(screen).move_cursor()
                        if event.key == pygame.K_w:
                            Menu.Mainmenu().UP_KEY1 = True
                            Menu.Choose_Ship_pl1(screen).move_cursor()
                        if event.key == pygame.K_i:
                            Menu.Mainmenu().UP_KEY2 = True
                            Menu.Choose_Ship_pl2(screen).move_cursor()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
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
