import pygame
from gameplay import *
from pygame.gfxdraw import *
from GameRes import *
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
Left_player = GameShipLeft(0, 0, 0,0,0,0,0,0,0,0,0,0,0,0, (0,0,0),10,10,0.01, 4, 10*60, 1,10*60)
Right_player = GameShipRight(0,0,0,0,0,0,0,0,0,0,0,0,0,0, (0,0,0),10,10,0.01, 4, 20*60, 3,10*60)

# создание классов игровых экранов - меню и и геймплея
gameplay_screen = Gameplay(Left_player, Right_player)
menu = Mainmenu()
choseShipLeft = Choose_Ship_pl1(menu)
choseShipRight = Choose_Ship_pl2(menu)
results = Game_res("jjsj", True)


while not finished:
    # для отрисовки интерфейса
    if screen_type == 'menu':
        gameplay_screen.reset()
        pygame.mixer.music.unload()
        gameplay_screen.time = 0
        menu.display_menutext(screen)
        choseShipLeft.display_menu(screen, choseShipLeft.move_cursor())
        choseShipRight.display_menu(screen, choseShipRight.move_cursor())
        menu.reset_keys()
        choseShipLeft.display_ship1(screen, choseShipLeft.move_cursor())
        menu.reset_keys()
        choseShipRight.display_ship2(screen, choseShipRight.move_cursor())
        menu.reset_keys()

    if screen_type == 'gameplay':
        gameplay_screen.time -= 1
        gameplay_screen.leftPl.DrawShip(screen)
        gameplay_screen.drawSpeedIndicators(screen, gameplay_screen.leftPl, 'left')
        gameplay_screen.drawSpeedIndicators(screen, gameplay_screen.rightPl, 'right')
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
        play_boom(gameplay_screen.torpeds)
        if gameplay_screen.leftPl.gameXP <= 2:
            screen_type = 'results'
            results.win_game = True
            results.winner_name = gameplay_screen.leftPl.name
            gameplay_screen.time = 0
            play_win_music()

        if gameplay_screen.rightPl.gameXP <= 2:
            screen_type = 'results'
            results.win_game = True
            results.winner_name = gameplay_screen.rightPl.name
            gameplay_screen.time = 0
            play_win_music()

        if gameplay_screen.time < 0:
            screen_type = 'results'
            results.win_game = False
            play_win_music()

    if screen_type == 'results':
        gameplay_screen.time -= 1
        if gameplay_screen.time >= -5 * FPS:
            results.draw(screen)
        else:
            screen_type = 'menu'

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
                        choseShipLeft.set_ships(gameplay_screen.leftPl, choseShipLeft.move_cursor())
                        gameplay_screen.leftPl.torped_tubes.clear()
                        gameplay_screen.leftPl.width = gameplay_screen.leftPl.new_image_0.get_width()
                        gameplay_screen.leftPl.height = gameplay_screen.leftPl.new_image_0.get_height()
                        choseShipRight.set_ships(gameplay_screen.rightPl, choseShipRight.move_cursor())
                        gameplay_screen.rightPl.width = gameplay_screen.rightPl.new_image_0.get_width()
                        gameplay_screen.rightPl.height = gameplay_screen.rightPl.new_image_0.get_height()
                        gameplay_screen.rightPl.torped_tubes.clear()
                        for i in range(0, gameplay_screen.leftPl.quantity_of_torpeds):
                            gameplay_screen.leftPl.torped_tubes.append(300 * 60)
                        for i in range(0, gameplay_screen.  rightPl.quantity_of_torpeds):
                            gameplay_screen.rightPl.torped_tubes.append(300 * 60)
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
            if screen_type == 'gameplay':
                gameplay_screen.leftPl.keyinput(event)
                gameplay_screen.rightPl.keyinput(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                    gameplay_screen.leftPl.fire_torped(gameplay_screen.torpeds,gameplay_screen.time)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
                    gameplay_screen.rightPl.fire_torped(gameplay_screen.torpeds,gameplay_screen.time)

pygame.quit()
