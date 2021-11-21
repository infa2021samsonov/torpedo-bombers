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
        self.font2 = pygame.font.SysFont('Rockwell', 80)

    def drawShips(self, screen):
        pass

    def drawInfo(self, screen):
        red_name_lable = self.font2.render("Bismark", True, (255, 255, 255), None)
        screen.blit(red_name_lable, (30, 30))
        green_name_lable = self.font2.render("Iowa", True, (255, 255, 255), None)
        screen.blit(green_name_lable, (1315, 30))

    def drawTime(self, screen):
        t = self.time // 60
        seconds = str(t % 60)
        if seconds == '0':
            seconds = '00'
        elif int(seconds) <= 9:
            seconds = '0' + seconds
        time_label = self.font1.render(str(t // 60) + ":" + seconds, True, (255, 255, 255), None)
        screen.blit(time_label, (750, 30))
        pass

    def drawTorpeds(self, screen):
        for i in range(0, len(self.torpeds)):
            if (self.torpeds[i].x <= 1600) and (self.torpeds[i].x >= 0) and (self.torpeds[i].y <= 900) and (
                    self.torpeds[i].y >= 0):
                self.torpeds[i].moveTorped()
                if self.torpeds[i].Hit(screen):
                    self.torpeds[i].detonation(screen)
                    self.torpeds.remove(self.torpeds[i])
                else:
                    screen.blit(self.torpeds[i].new_image, (self.torpeds[i].x, self.torpeds[i].y))
            else:
                self.torpeds.remove(self.torpeds[i])

    def drawTorpedIndicators(self, screen, player: GameShip, left_or_right):
        x = 0
        y = 0
        a = 40
        gap = 15
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
                height = k * a
                pygame.draw.rect(screen, (255, 255, 255), (x, y + (a - height), a, height))
            x = x + (a + gap)


