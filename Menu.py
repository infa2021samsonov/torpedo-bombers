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
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN
        self.startx, self.starty = self.mid_w, self.mid_h
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.player2x, self.player2y = self.mid_w * 3 // 2, self.mid_h // 2

    def check_events(self):
        '''
        Функция проверяет нажаие клвиш
        :return:
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_s:
                    self.DOWN_KEY1 = True
                if event.key == pygame.K_k:
                    self.DOWN_KEY2 = True
                if event.key == pygame.K_w:
                    self.UP_KEY1 = True
                if event.key == pygame.K_i:
                    self.UP_KEY2 = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self,screen, text, size, x, y):
        '''
        Функция позволяющая отображать надписи.
        :return:
        '''
        font = pygame.font.SysFont('Rockwell', size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def display_menutext(self, screen):
        '''
        Функция отображает надписи в меню
        :return:
        '''
        self.draw_text(screen, 'Player 1', 20, self.player1x, self.player1y)
        self.draw_text(screen, 'Player 2', 20, self.player2x, self.player2y)
        self.draw_text(screen, 'PLAY', 20, self.startx, self.starty)

    def setShips(self, ):

        pass

class Choose_Ship_pl1():
    def __init__(self, mainmenu: Mainmenu):
        self.offset = -100
        self.mainmenu = mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1500, 800
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY1, self.DOWN_KEY1, self.START_KEY1, self.BACK_KEY1 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_1x, self.boatname1_1y = self.mid_w // 2, self.mid_h // 2 + 30
        self.boatname2_1x, self.boatname2_1y = self.mid_w // 2, self.mid_h // 2 + 60
        self.boatname3_1x, self.boatname3_1y = self.mid_w // 2, self.mid_h // 2 + 90
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.state = 'Bismark'

    def display_menu(self, screen):
        '''
        Функция отображает название кораблей для игрока 1
        :return:
        '''
        #self.mainmenu.check_events()
        self.mainmenu.draw_text(screen, 'Main Menu', 20, self.DISPLAY_W // 2, 20)
        self.mainmenu.draw_text(screen, 'Bismark', 15, self.boatname1_1x, self.boatname1_1y)
        self.mainmenu.draw_text(screen, 'Iowa', 15, self.boatname2_1x, self.boatname2_1y)
        self.mainmenu.draw_text(screen, 'Yamato', 15, self.boatname3_1x, self.boatname3_1y)


    def move_cursor(self):
        if self.mainmenu.DOWN_KEY1:
            if self.state == 'Bismark':
                self.cursor_rect.midtop = (self.boatname1_1x + self.offset, self.boatname1_1y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.cursor_rect.midtop = (self.boatname2_1x + self.offset, self.boatname2_1y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.cursor_rect.midtop = (self.boatname3_1x + self.offset, self.boatname3_1y)
                self.state = 'Bismark'
        elif self.mainmenu.UP_KEY1:
            if self.state == 'Bismark':
                self.cursor_rect.midtop = (self.boatname1_1x + self.offset, self.boatname1_1y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.cursor_rect.midtop = (self.boatname3_1x + self.offset, self.boatname3_1y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.cursor_rect.midtop = (self.boatname2_1x + self.offset, self.boatname2_1y)
                self.state = 'Bismark'


class Choose_Ship_pl2:
    def __init__(self, mainmenu: Mainmenu):
        self.offset = -100
        self.mainmenu = mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1500, 800
        self.font_name = pygame.font.get_default_font()
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY2, self.DOWN_KEY2, self.START_KEY2, self.BACK_KEY2 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_2x, self.boatname1_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 30
        self.boatname2_2x, self.boatname2_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 60
        self.boatname3_2x, self.boatname3_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 90
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.state = 'Bismark'
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN


    def display_menu(self, screen):
        '''
        Функция отображает название кораблей для игрока 2
        :return:
        '''
        #self.mainmenu.check_events()
        self.mainmenu.draw_text(screen, 'Main Menu', 20, self.DISPLAY_W // 2, 20)
        self.mainmenu.draw_text(screen, 'Bismark', 15, self.boatname1_2x, self.boatname1_2y)
        self.mainmenu.draw_text(screen, 'Iowa', 15, self.boatname2_2x, self.boatname2_2y)
        self.mainmenu.draw_text(screen, 'Yamato', 15, self.boatname3_2x, self.boatname3_2y)

    def move_cursor(self):
        if self.mainmenu.DOWN_KEY2:
            if self.state == 'Bismark':
                self.cursor_rect.midtop = (self.boatname1_2x + self.offset, self.boatname1_2y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.cursor_rect.midtop = (self.boatname2_2x + self.offset, self.boatname2_2y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.cursor_rect.midtop = (self.boatname3_2x + self.offset, self.boatname3_2y)
                self.state = 'Bismark'
        elif self.mainmenu.UP_KEY2:
            if self.state == 'Bismark':
                self.cursor_rect.midtop = (self.boatname1_2x + self.offset, self.boatname1_2y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.cursor_rect.midtop = (self.boatname3_2x + self.offset, self.boatname3_2y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.cursor_rect.midtop = (self.boatname2_2x + self.offset, self.boatname2_2y)
                self.state = 'Bismark'