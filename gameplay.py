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
        time_label = self.font1.render(str(t // 60) + ":" + seconds, True, (255, 255, 255), None)
        screen.blit(time_label, (750, 30))
        pass

    def drawTorpeds(self, screen):
        for i in range(0, len(self.torpeds)):
            if (self.torpeds[i].x <= 1600) and (self.torpeds[i].x >= 0) and (self.torpeds[i].y <= 900) and (self.torpeds[i].y >= 0):
                self.torpeds[i].moveTorped()
                if self.torpeds[i].Hit(screen):
                    self.torpeds[i].detonation(screen)
                    self.torpeds.remove(self.torpeds[i])
                else:
                    screen.blit(self.torpeds[i].new_image, (self.torpeds[i].x, self.torpeds[i].y))
            else:
                self.torpeds.remove(self.torpeds[i])

# Класс для отрисовки в геймплее индикаторов торпедных аппаратов
class torped_recharge_units:

    def __init__(self, player, x, y):
        self.x = x
        self.y = y
        self.a = 30
        self.gap = 20
        self.last_recharge_times = []

    def draw_n_block(self, n, screen, nowtime):
        # не работает нифига, но это временно
        for i in range(1, self.n):
            x = self.x + (n - 1) * (self.a + self.gap)
            y = self.y
            rectangle(screen, (x, y, x + self.a, y + self.a), (160, 160, 160))
            if (nowtime - self.last_recharge_time) >= self.time_recharge:
                rectangle(screen, (x, y, x + self.a, y + self.a), (255, 255, 255))
            else:
                k = (nowtime - self.last_recharge_time) / self.time_recharge
                height = k * self.a
                rectangle(screen, (x, y + (self.a - height), x + self.a , y + self.a), (255, 255, 255))






