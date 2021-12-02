import pygame
from gameplay import *
from pygame.gfxdraw import *
from Menu import *
from gameplay import *
from ModelShip import *

pygame.init()
# еще возможно  'gameplay'
screen_type = 'menu'
# цвет моря
sea_color = (62, 145, 179)

FPS = 60
DISPLAY_W = 1600
DISPLAY_H = 900
screen = pygame.display.set_mode((1600, 900))
screen.fill(sea_color)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Это над для создания класса геймплея - не трогать и не смотреть
Left_player = GameShip(100,1,1,1,0,0,0,70.7,50,50,10,10, (0,0,0),10,10,0.01, 4, 10*60, 1,10*60)
Right_player = GameShip(100,1,1,1,0,0,0,70.7,50,50,10,10, (0,0,0),10,10,0.01, 4, 20*60, 3,10*60)

# создание классов игровых экранов - меню и и геймплея
gameplay_screen = Gameplay(Left_player, Right_player)
menu = Mainmenu()
choseShipLeft = Choose_Ship_pl1(menu)
choseShipRight = Choose_Ship_pl2(menu)
# Экран меню Андрея


while not finished:
    # для отрисовки интерфейса
    if screen_type == 'menu':
        gameplay_screen.time = 0
        menu.display_menutext(screen)
        choseShipLeft.display_menu(screen, choseShipLeft.move_cursor())
        #menu.reset_keys()
        choseShipRight.display_menu(screen, choseShipRight.move_cursor())
        menu.reset_keys()
        choseShipLeft.display_ship1(screen, choseShipLeft.move_cursor())
        menu.reset_keys()
        choseShipRight.display_ship2(screen, choseShipRight.move_cursor())
        menu.reset_keys()

    if screen_type == 'gameplay':
        gameplay_screen.time -= 1
        gameplay_screen.leftPl.DrawShip(screen)
        gameplay_screen.rightPl.DrawShip(screen)
        gameplay_screen.rightPl.Move(gameplay_screen.torpeds)
        gameplay_screen.leftPl.Move(gameplay_screen.torpeds)
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu.START_KEY = True
                        screen_type = 'gameplay'
                        gameplay_screen.time = 300 * FPS
                        print("hi")
                    if event.key == pygame.K_BACKSPACE:
                        menu.BACK_KEY = True
                    if event.key == pygame.K_s:
                        menu.DOWN_KEY1 = True
                        choseShipLeft.move_cursor()
                    if event.key == pygame.K_k:
                        menu.DOWN_KEY2 = True
                        choseShipLeft.move_cursor()
                    if event.key == pygame.K_w:
                        menu.UP_KEY1 = True
                        choseShipLeft.move_cursor()
                    if event.key == pygame.K_i:
                        menu.UP_KEY2 = True
                        choseShipRight.move_cursor()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                    screen_type = 'gameplay'
                    gameplay_screen.time = 300*FPS

            if screen_type == 'gameplay':
                gameplay_screen.leftPl.keyinput(event)
                gameplay_screen.rightPl.keyinput(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                    gameplay_screen.leftPl.fire_torped(gameplay_screen.torpeds,gameplay_screen.time)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
                    gameplay_screen.rightPl.fire_torped(gameplay_screen.torpeds,gameplay_screen.time)

pygame.quit()
