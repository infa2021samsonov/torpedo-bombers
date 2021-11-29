import os
import sys

from Torped_classes import *
import pygame
from ModelShip import *
from pygame.gfxdraw import *


class Gameplay:
    def __init__(self, pl1, pl2):
        self.torpeds = []
        self.time = 0
        pygame.font.init()
        # Экземпляры кораблей,  свойства которых надо устанавливать при нажатии Play
        self.leftPl: GameShip = pl1
        self.rightPl: GameShip = pl2
        self.font1 = pygame.font.SysFont('Rockwell', 60)
        self.font2 = pygame.font.SysFont('Rockwell', 60)

    def drawInfo(self, screen):
        gap = 15
        red_name_lable = self.font2.render("Bismark", True, (255, 255, 255), None)
        screen.blit(red_name_lable, (gap, gap))
        green_name_lable = self.font2.render("Iowa", True, (255, 255, 255), None)
        screen.blit(green_name_lable, (1600 - gap - green_name_lable.get_width(), gap))

    def drawTime(self, screen):
        t = self.time // 60
        seconds = str(t % 60)
        if seconds == '0':
            seconds = '00'
        elif int(seconds) <= 9:
            seconds = '0' + seconds
        time_label = self.font1.render(str(t // 60) + ":" + seconds, True, (255, 255, 255), None)
        screen.blit(time_label, (750, 15))
        pass

    def drawTorpeds(self, screen):
        for i in range(0, len(self.torpeds)):
            self.torpeds[i].moveTorped()
            screen.blit(self.torpeds[i].new_image, (self.torpeds[i].x, self.torpeds[i].y))

    def drawTorpedIndicators(self, screen, player: GameShip, left_or_right):
        x = 0
        y = 0
        a = 38
        gap = 14
        if left_or_right == 'left':
            x = gap
            y = 900 - gap - a
        if left_or_right == 'right':
            x = 1600 - (gap + a) * player.quantity_of_torpeds
            y = 900 - gap - a

        for i in range(0, player.quantity_of_torpeds):
            pygame.draw.rect(screen, (160, 160, 160), (x, y, a, a))
            if (player.torped_tubes[i] - self.time) >= player.recharge_time:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, a, a))
            else:
                k = (player.torped_tubes[i] - self.time) / player.recharge_time
                height = k * (a-6)
                pygame.draw.rect(screen, (255, 255, 255), (x + 3, y + ((a-6) - height) + 3, a - 6, height ))
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            image = pygame.image.load(path + '/torpedo.png').convert_alpha()
            new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.07), int(image.get_height() * 0.07)))
            new_image = pygame.transform.rotate(new_image_0, 45)
            screen.blit(new_image, (x + 0.14 * a, y + 0.12 * a))
            x = x + (a + gap)

    def drawXP(self, screen, player: GameShip, left_or_right):
        x = 0
        y = 80
        gap = 15
        a = 12
        l = 300
        if left_or_right == 'left':
            x = gap
            pygame.draw.rect(screen, (160, 160, 160), (x, y, l, a))
            pygame.draw.rect(screen, (255, 255, 255), (x, y, (player.gameXP/player.maxXP) * l, a))
        if left_or_right == 'right':
            x = 1600 - gap - l
            pygame.draw.rect(screen, (160, 160, 160), (x, y, l, a))
            pygame.draw.rect(screen, (255, 255, 255), (x + (l - (player.gameXP / player.maxXP) * l), y, (player.gameXP / player.maxXP) * l, a))



