import pygame
#from Ship_types import *
import time
import thorpy
from colors import *
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


timer = None
finished = False

FPS = 30
width = 1080
height = 720


pos_red = (40, 40)
pos_green = (width - 180, 40)

class buttons:
    def __init__(self):
        self.finished = False


    def stop_execution(self):
        self.finished = True

    def start_execution(self):
        pass

    def init_ui(screen):


        button_stop = thorpy.make_button("Quit", func = buttons.stop_execution)
        button_play = thorpy.make_button("Play", func = buttons.start_execution)
        timer = thorpy.OneLineText("Seconds passed")

        box = thorpy.Box(elements=[button_play, button_stop])
        reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},)
        box.add_reaction(reaction1)

        menu = thorpy.Menu(box)
        for element in menu.get_population():
            element.surface = screen

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
        :param num: в.
        :return:
        '''
        text = self.my_font.render(self.pre_text, 2, self.color)
        self.surface.blit(text, (self.pos))



pygame.init()
screen = pygame.display.set_mode((width, height))


finished = False
clock = pygame.time.Clock()
rect = ()
player_1 = Work_Field(screen, pos_red, "RED", RED)
player_2 = Work_Field(screen, pos_green, "GREEN", GREEN)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break


    pygame.display.update()
    screen.fill(CYAN)


    player_1.write()
    player_2.write()
pygame.quit()