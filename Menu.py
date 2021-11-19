import pygame
#from Ship_types import *
import time
import thorpy
from pygame.draw import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (168, 203, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (30, 62, 226)
BLACK = (0, 0, 0)
DARKGREEN = (7, 95, 7)
GOLD = (212, 175, 55)



class buttons:
    def __init__(self, finished):
        self.finished = finished


    def stop_execution(self):
        self.finished = True

    def start_execution(self):
        pass

    def init_ui(self):

        button_quit = thorpy.make_button("Quit", func = thorpy.functions.quit_func)
        button_play = thorpy.make_button("Play", func = buttons.start_execution)


        box = thorpy.Box(elements=[button_play, button_quit])
        reaction1 = thorpy.Reaction

class Work_Field:
    def __init__(self, surface, pos, pre_text, color):
        self.surface = surface
        self.my_font = pygame.font.Font(None, 50)
        self.pos = pos
        self.pre_text = pre_text
        self.color = color

    def write(self):
        '''
        Функция выводит надпись.

        :return:
        '''
        text = self.my_font.render(self.pre_text, 2, self.color)
        self.surface.blit(text, (self.pos))



