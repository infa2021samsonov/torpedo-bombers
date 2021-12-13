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
        self.leftPl: GameShipLeft = pl1
        self.rightPl: GameShipRight = pl2
        self.font1 = pygame.font.SysFont('Rockwell', 60)
        self.font2 = pygame.font.SysFont('Rockwell', 60)

    def drawInfo(self, screen):
        gap = 15
        red_name_lable = self.font2.render(self.leftPl.name, True, (255, 255, 255), None)
        screen.blit(red_name_lable, (gap, gap))
        green_name_lable = self.font2.render(self.rightPl.name, True, (255, 255, 255), None)
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
            if self.torpeds[i].hit:
                if self.torpeds[i].k <= 25:
                    if (self.torpeds[i].hit_time - self.time) % 7 == 0:
                        self.torpeds[i].k += 1
                    path = os.path.abspath(os.path.dirname(sys.argv[0]))
                    image = pygame.image.load(path + '/Boompict/' + str(self.torpeds[i].k) + ".png").convert_alpha()
                    image = pygame.transform.scale(image, (int(image.get_width() * 0.3), int(image.get_height() * 0.3)))
                    screen.blit(image, (self.torpeds[i].x - image.get_width()/2, self.torpeds[i].y - image.get_height()/2))
            else:
                self.torpeds[i].moveTorped()
                screen.blit(self.torpeds[i].new_image, (self.torpeds[i].x - self.torpeds[i].w/2, self.torpeds[i].y - self.torpeds[i].h/2))

                if self.leftPl.collision(self.torpeds[i]):
                    #строка для уменьшения ХP
                    self.torpeds[i].hit = True
                    self.torpeds[i].just_hit = True
                    self.torpeds[i].hit_time = self.time
                    print("попало в левого")

                if self.rightPl.collision(self.torpeds[i]):
                    #строка для уменьшения ХP
                    self.torpeds[i].hit = True
                    self.torpeds[i].just_hit = True
                    self.torpeds[i].hit_time = self.time
                    print("попало в правого")

    def drawTorpedIndicators(self, screen, player, left_or_right):
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

    def drawXP(self, screen, player, left_or_right):
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

    def reset(self):
        self.torpeds.clear()
        self.time = 0
        self.leftPl.torped_tubes.clear()
        self.rightPl.torped_tubes.clear()

    def same_orientation(self, player):
        x1 = -sin(player.alpha)
        y1 = -cos(player.alpha)
        x2 = player.Vx
        y2 = player.Vy
        return x1*x2 + y1*y2 <=0
    def drawSpeedIndicators(self, screen, player, left_or_right):
        x = 0
        y = 0
        a = 10
        b = 20
        k = 0
        if left_or_right == "left":
            x = 100
            y = 100
        elif left_or_right == "right":
            x = 500
            y = 500
        if self.same_orientation(player):
            k = sqrt(player.Vx**2 + player.Vy**2) / sqrt(player.Vxmax**2 + player.Vymax**2)
            pygame.draw.rect(screen, (160, 160, 160), (x, y, a, b))
            pygame.draw.rect(screen,(0,255,0), (x, y + b/2 - b/2 * k,a, b/2 * k))

def play_boom(arr):
    for i in range(0,len(arr)):
        if arr[i].just_hit:
            arr[i].just_hit = False
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
            pygame.mixer.music.load(path + '/Boom.mp3')
            pygame.mixer.music.play()