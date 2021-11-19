from Torped import *
import pygame
from ModelShip import *
from pygame.gfxdraw import *

class Gameplay:
    def __init__(self, pl1, pl2):
        self.torpeds = [Torped]
        self.time = 300
        pygame.font.init()
        self.leftPl = pl1
        self.rightPl = pl2
        self.font1 = pygame.font.SysFont('Rockwell', 60)
        self.font2 = pygame.font.SysFont('Rockwell', 80)

    def drawShips(self, screen):
        pass

    def drawInfo(self, screen):
        red_name_lable = self.font2.render("Bismark", True, (255, 255, 255), None)
        screen.blit(red_name_lable, (30, 30))
        green_name_lable = self.font2.render("Yowa", True, (255, 255, 255), None)
        screen.blit(green_name_lable, (1315, 30))

    def drawTime(self, screen):
        seconds = str(self.time % 60)
        if seconds == '0':
            seconds = '00'
        time_label = self.font1.render(str(self.time // 60) + ":" + seconds, True, (255, 255, 255), None)
        screen.blit(time_label, (750, 30))
        pass

    def drawTorpeds(self, screen):
        for i in self.torpeds:
            if (i.x <= 1600) and (i.x >= 0) and (i.y <= 900) and (i.y >= 0):
                i.moveTorped()
                if i.Hit():
                    i.detonation()
                    self.torpeds.remove(i)
                else:
                    screen.blit(i.new_image, (i.x, i.y))
            else:
                self.torpeds.remove(i)


class torped_recharge_units:

    def __init__(self, n, x, y, t):
        self.n = n
        self.x = x
        self.y = y
        self.a = 30
        self.time_recharge = t
        self.gap = 20
        self.last_recharge_times = []

    def draw_n_block(self, n, screen, nowtime):
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






