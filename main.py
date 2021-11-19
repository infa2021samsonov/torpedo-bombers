import pygame
from gameplay import *
from pygame.draw import *
from gameplay import *
pygame.init()
screen_type = 'menu'
sea_color = (62, 145, 179)
FPS = 30
screen = pygame.display.set_mode((1600, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen.fill(sea_color)
#======Для тестирования===========
game = Gameplay()
game.drawTime(screen)
game.drawInfo(screen)
#=================================
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_type == 'menu':
                print("Андрей")

            if screen_type == 'gameplay':

                print("Сом")

pygame.quit()