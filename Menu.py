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
        self.screen_type = "menu"
        self.running = True
        self.playing = False
        self.DISPLAY_W, self.DISPLAY_H = 1500, 800
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN
        self.display.fill(self.CYAN)
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

    def blit_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        self.reset_keys()

    def draw_text(self, text, size, x, y):
        '''
        Функция позволяющая отображать надписи.
        :return:
        '''
        self.font = pygame.font.SysFont(self.font_name, size)
        self.text_surface = self.font.render(text, True, self.WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (x, y)
        self.display.blit(self.text_surface, self.text_rect)

    def display_menutext(self, screen):
        '''
        Функция отображает надписи в меню
        :return:
        '''
        self.run_display = True
        self.surface = screen
        while self.run_display:
            self.draw_text('Player 1', 20, self.player1x, self.player1y)
            self.draw_text('Player 2', 20, self.player2x, self.player2y)
            self.draw_text('PLAY', 20, self.startx, self.starty)

class Choose_Ship_pl1():
    def __init__(self, Mainmenu):
        self.offset = -100
        self.Mainmenu = Mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1500, 800
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY1, self.DOWN_KEY1, self.START_KEY1, self.BACK_KEY1 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_1x, self.boatname1_1y = self.mid_w // 2, self.mid_h // 2 + 30
        self.boatname2_1x, self.boatname2_1y = self.mid_w // 2, self.mid_h // 2 + 60
        self.boatname3_1x, self.boatname3_1y = self.mid_w // 2, self.mid_h // 2 + 90
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)

    def display_menu(self, screen):
        '''
        Функция отображает название кораблей для игрока 1
        :return:
        '''
        self.run_display = True
        self.surface = screen
        while self.run_display:
            self.Mainmenu.check_events()
            self.Mainmenu.draw_text('Main Menu', 20, self.DISPLAY_W // 2, 20)
            self.Mainmenu.draw_text('Bismark', 15, self.boatname1_1x, self.boatname1_1y)
            self.Mainmenu.draw_text('Iowa', 15, self.boatname2_1x, self.boatname2_1y)
            self.Mainmenu.draw_text('Yamato', 15, self.boatname3_1x, self.boatname3_1y)


    def move_cursor(self):
        if self.Mainmenu.DOWN_KEY1:
            if self.state == 'Bismark':
                self.cursor_rect.midtop = (self.boatname1_1x + self.offset, self.boatname1_1y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.cursor_rect.midtop = (self.boatname2_1x + self.offset, self.boatname2_1y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.cursor_rect.midtop = (self.boatname3_1x + self.offset, self.boatname3_1y)
                self.state = 'Bismark'
        elif self.Mainmenu.UP_KEY1:
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
    def __init__(self, Mainmenu):
        self.offset = -100
        self.Mainmenu = Mainmenu
        self.DISPLAY_W, self.DISPLAY_H = 1500, 800
        self.font_name = pygame.font.get_default_font()
        self.mid_w, self.mid_h = self.DISPLAY_W // 2, self.DISPLAY_H // 2
        self.UP_KEY2, self.DOWN_KEY2, self.START_KEY2, self.BACK_KEY2 = False, False, False, False
        self.player1x, self.player1y = self.mid_w // 2, self.mid_h // 2
        self.boatname1_2x, self.boatname1_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 30
        self.boatname2_2x, self.boatname2_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 60
        self.boatname3_2x, self.boatname3_2y = self.mid_w * 3 // 2, self.mid_h // 2 + 90
        self.WHITE, self.BLACK, self.CYAN = WHITE, BLACK, CYAN


    def display_menu(self, screen):
        '''
        Функция отображает название кораблей для игрока 2
        :return:
        '''
        self.run_display = True
        self.surface = screen
        while self.run_display:
            self.Mainmenu.check_events()
            self.Mainmenu.draw_text('Main Menu', 20, self.DISPLAY_W // 2, 20)
            self.Mainmenu.draw_text('Bismark', 15, self.boatname1_2x, self.boatname1_2y)
            self.Mainmenu.draw_text('Iowa', 15, self.boatname2_2x, self.boatname2_2y)
            self.Mainmenu.draw_text('Yamato', 15, self.boatname3_2x, self.boatname3_2y)

    def move_cursor(self):
        if self.Mainmenu.DOWN_KEY2:
            if self.state == 'Bismark':
                self.Mainmenu.cursor_rect.midtop = (self.boatname1_2x + self.offset, self.boatname1_2y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.Mainmenu.cursor_rect.midtop = (self.boatname2_2x + self.offset, self.boatname2_2y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.Mainmenu.cursor_rect.midtop = (self.boatname3_2x + self.offset, self.boatname3_2y)
                self.state = 'Bismark'
        elif self.Mainmenu.UP_KEY2:
            if self.state == 'Bismark':
                self.Mainmenu.cursor_rect.midtop = (self.boatname1_2x + self.offset, self.boatname1_2y)
                self.state = 'Yamato'
            elif self.state == 'Yamato':
                self.Mainmenu.cursor_rect.midtop = (self.boatname3_2x + self.offset, self.boatname3_2y)
                self.state = 'Iowa'
            elif self.state == 'Iowa':
                self.Mainmenu.cursor_rect.midtop = (self.boatname2_2x + self.offset, self.boatname2_2y)
                self.state = 'Bismark'