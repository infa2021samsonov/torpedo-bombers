import os
import sys

import pygame


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (168, 203, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 79, 255)
BLACK = (0, 0, 0)
DARKGREEN = (7, 95, 7)
GOLD = (212, 175, 55)



class Mainmenu():
    def __init__(self):
        self.running = True
        self.playing = False
        self.DISPLAY_W, self.DISPLAY_H = 1600, 900
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.UP_KEY1, self.DOWN_KEY1, self.UP_KEY2, self.DOWN_KEY2, self.START_KEY1, = False, False, False, False, False
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN
        self.startx, self.starty = self.mid_w, self.mid_h * 3 // 2
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.player2x, self.player2y = self.mid_w * 3 // 2, self.mid_h // 2

    def check_events(self):
        '''
        Функция проверяет нажаие клвиш.
        :return:
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_s:
                    self.DOWN_KEY1 = True
                if event.key == pygame.K_k:
                    self.DOWN_KEY2 = True
                if event.key == pygame.K_w:
                    self.UP_KEY1 = True
                if event.key == pygame.K_i:
                    self.UP_KEY2 = True

    def reset_keys(self):
        self.UP_KEY1, self.DOWN_KEY1, self.UP_KEY2, self.DOWN_KEY2, self.START_KEY1, = False, False, False, False, False

    def draw_text(self,screen, text, size, x, y, color):
        '''
        Функция позволяющая отображать надписи.
        :return:
        '''
        font = pygame.font.SysFont('Rockwell', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def display_menutext(self, screen):
        '''
        Функция отображает надписи в меню
        :return:
        '''
        self.draw_text(screen, 'MAIN MENU', 60, self.mid_w, 60, WHITE)
        self.draw_text(screen, 'NIGGER 1', 30, self.player1x, self.player1y, RED)
        self.draw_text(screen, 'NIGGER 2', 30, self.player2x, self.player2y, GREEN)
        self.draw_text(screen, 'PRESS ''ENTER'' TO START THE GAME', 50, self.startx, self.starty, WHITE)

    def setShips(self, state):

        pass

class Choose_Ship_pl1():
    def __init__(self, mainmenu: Mainmenu):
        self.offset = -100
        self.mainmenu = mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1600, 900
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY1, self.DOWN_KEY1, self.START_KEY1, self.BACK_KEY1 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_1x, self.boatname1_1y = self.mid_w // 2, self.mid_h // 2 + 60
        self.boatname2_1x, self.boatname2_1y = self.mid_w // 2, self.mid_h // 2 + 120
        self.boatname3_1x, self.boatname3_1y = self.mid_w // 2, self.mid_h // 2 + 180
        self.shippos1x, self.shippos1y = self.mid_w - 260, self.mid_h // 2 + 80
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.state = 'Bismark'


    def move_cursor(self):
        '''
            Функция выделяет название выбранного корабля
            :return:подсвеченный текст
        '''
        if self.mainmenu.DOWN_KEY1:
            if self.state == 'Bismark':
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.state = 'Bismark'
        elif self.mainmenu.UP_KEY1:
            if self.state == 'Bismark':
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.state = 'Bismark'
        return self.state


    def display_menu(self, screen, state):
        if state == 'Bismark':
            self.mainmenu.draw_text(screen, 'Bismark', 70, self.boatname1_1x, self.boatname1_1y, GOLD)
            self.mainmenu.draw_text(screen, 'Iowa', 40, self.boatname2_1x, self.boatname2_1y + 15, WHITE)
            self.mainmenu.draw_text(screen, 'Yamato', 40, self.boatname3_1x, self.boatname3_1y + 15, WHITE)
        elif state == 'Iowa':
            self.mainmenu.draw_text(screen, 'Bismark', 40, self.boatname1_1x, self.boatname1_1y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Iowa', 70, self.boatname2_1x, self.boatname2_1y , GOLD)
            self.mainmenu.draw_text(screen, 'Yamato', 40, self.boatname3_1x, self.boatname3_1y + 15, WHITE)
        elif state == 'Yamato':
            self.mainmenu.draw_text(screen, 'Bismark', 40, self.boatname1_1x, self.boatname1_1y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Iowa', 40, self.boatname2_1x, self.boatname2_1y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Yamato', 70, self.boatname3_1x, self.boatname3_1y, GOLD)


    def display_ship1(self, screen, state):
        '''
        Функция отображанет изображение корабля выбранного игроком 1

        :param screen: экран....
        :param state: конкретный выбранный корабль
        :return: картиночу отображает
        '''
        if state == 'Bismark':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/Bismark_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            img_with_flip = pygame.transform.flip(new_image_0, True, False)
            self.new_image = pygame.transform.rotate(img_with_flip, 0)
            screen.blit(self.new_image, (self.shippos1x, self.shippos1y))
        elif state == 'Iowa':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/IOWA_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            img_with_flip = pygame.transform.flip(new_image_0, True, False)
            self.new_image = pygame.transform.rotate(img_with_flip, 0)
            screen.blit(self.new_image, (self.shippos1x, self.shippos1y))
        elif state == 'Yamato':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/Yamato_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            img_with_flip = pygame.transform.flip(new_image_0, True, False)
            self.new_image = pygame.transform.rotate(img_with_flip, 0)
            screen.blit(self.new_image, (self.shippos1x, self.shippos1y))

class Choose_Ship_pl2:
    def __init__(self, mainmenu: Mainmenu):
        self.offset = -100
        self.mainmenu = mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1600, 900
        self.font_name = pygame.font.get_default_font()
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY2, self.DOWN_KEY2, self.START_KEY2, self.BACK_KEY2 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_2x, self.boatname1_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 60
        self.boatname2_2x, self.boatname2_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 120
        self.boatname3_2x, self.boatname3_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 180
        self.shippos2x, self.shippos2y = self.mid_w + 70, self.mid_h // 2 + 80
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.state = 'Bismark'
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN



    def move_cursor(self):
        '''
            Функция выделяет название выбранного корабля
            :return:подсвеченный текст
        '''
        if self.mainmenu.DOWN_KEY2:
            if self.state == 'Bismark':
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.state = 'Bismark'
        elif self.mainmenu.UP_KEY2:
            if self.state == 'Bismark':
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.state = 'Bismark'
        return self.state

    def display_menu(self, screen, state):
        '''
        Функция отображает название кораблей для игрока 2
        :return:
        '''
        if state == 'Bismark':
            self.mainmenu.draw_text(screen, 'Bismark', 70, self.boatname1_2x, self.boatname1_2y, GOLD)
            self.mainmenu.draw_text(screen, 'Iowa', 40, self.boatname2_2x, self.boatname2_2y + 15, WHITE)
            self.mainmenu.draw_text(screen, 'Yamato', 40, self.boatname3_2x, self.boatname3_2y + 15, WHITE)
        elif state == 'Iowa':
            self.mainmenu.draw_text(screen, 'Bismark', 40, self.boatname1_2x, self.boatname1_2y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Iowa', 70, self.boatname2_2x, self.boatname2_2y , GOLD)
            self.mainmenu.draw_text(screen, 'Yamato', 40, self.boatname3_2x, self.boatname3_2y + 15, WHITE)
        elif state == 'Yamato':
            self.mainmenu.draw_text(screen, 'Bismark', 40, self.boatname1_2x, self.boatname1_2y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Iowa', 40, self.boatname2_2x, self.boatname2_2y - 15, WHITE)
            self.mainmenu.draw_text(screen, 'Yamato', 70, self.boatname3_2x, self.boatname3_2y, GOLD)

    def display_ship2(self, screen, state):
        '''
            Функция отображанет изображение корабля выбранного игроком 2

            :param screen: экран....
            :param state: конкретный выбранный корабль
            :return: картиночу отображает
        '''
        if state == 'Bismark':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/Bismark_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            self.new_image = pygame.transform.rotate(new_image_0, 0)
            screen.blit(self.new_image, (self.shippos2x, self.shippos2y))
        elif state == 'Iowa':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/IOWA_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            self.new_image = pygame.transform.rotate(new_image_0, 0)
            screen.blit(self.new_image, (self.shippos2x, self.shippos2y))
        elif state == 'Yamato':
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/Yamato_side-removebg-preview.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.22), int(image.get_height() * 0.22)))
            self.new_image = pygame.transform.rotate(new_image_0, 0)
            screen.blit(self.new_image, (self.shippos2x, self.shippos2y))