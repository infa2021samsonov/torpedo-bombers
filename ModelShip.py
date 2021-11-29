import math
import os
import sys
from Torped_classes import *
from random import choice
from random import randint
import pygame

FPS = 30

StartXP = [100, 200, 300]

RED = 0xFF0000
GREEN = 0x00FF00

COLOR = [RED, GREEN]
FORCE = [100, 200, 300]
TURNFORCE = [10, 20, 30]
MASS = [1000, 2000, 3000]


class GameShip:
    def __init__(self, m, b, x, y, alpha, Vmax, Vxmax, Vymax, Vx, Vy, a, omega, gameXP, color, F, TF, dt, maxXP,
                 quantity_of_torpeds, recharge_time):
        self.maxXP = maxXP
        self.m = choice(MASS)
        self.b = 0.01
        self.x = 450
        self.y = 20
        self.alpha = 0
        self.Vmax = 70.7
        self.Vxmax = 50
        self.Vymax = 50
        self.Vx = 0
        self.Vy = 0
        self.a = 5
        self.omega = 0.1
        self.gameXP = maxXP / 2
        self.color = choice(COLOR)
        self.F = choice(FORCE)
        self.TF = choice(TURNFORCE)
        self.dt = 0.1
        self.kw = False
        self.ks = False

        self.ka = False
        self.kd = False
        self.kshift = False
        # Количество торпедных аппаратов у данного корабля и время их перезарядки
        self.quantity_of_torpeds = quantity_of_torpeds
        self.recharge_time = recharge_time
        # создание массива в котором хранится время последнего заряжания этого i-го торпедного аппарата
        self.torped_tubes = []
        for i in range(0, self.quantity_of_torpeds):
            self.torped_tubes.append(300 * 60)
        # это сделано Сомом для отображения

    def keyinput(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                self.kw = True
            if event.key == pygame.K_s:
                self.ks = True
            if event.key == pygame.K_a:
                self.ka = True
            if event.key == pygame.K_d:
                self.kd = True
            if event.key == pygame.K_LSHIFT:
                self.kshift = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.kw = False
            if event.key == pygame.K_s:
                self.ks = False
            if event.key == pygame.K_a:
                self.ka = False
            if event.key == pygame.K_d:
                self.kd = False
            if event.key == pygame.K_LSHIFT:
                self.kshift = False

    def DrawShip(self, screen):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        image = pygame.image.load(path + '/IOWA_top-removebg-preview.png').convert_alpha()
        new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.15), int(image.get_height() * 0.15)))
        self.new_image = pygame.transform.rotate(new_image_0, (self.alpha + math.pi / 2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x, self.y))
        pass

    def Move(self, torp_arr):
        if self.kw == True:
            if abs(self.Vx) <= self.Vxmax and abs(self.Vy) <= self.Vymax:
                self.Vx = self.Vx - self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.Vy - self.a * math.cos(self.alpha) * self.dt
                self.x = self.x - self.Vx * self.dt
                self.y = self.y - self.Vy * self.dt
            else:
                self.x = self.x - self.Vmax * math.sin(self.alpha) * self.dt
                self.y = self.y - self.Vmax * math.cos(self.alpha) * self.dt
        if self.ks == True:
            if abs(self.Vx) <= self.Vxmax and abs(self.Vy) <= self.Vymax:
                self.Vx = self.Vx + self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.y + self.a * math.cos(self.alpha) * self.dt
                self.x = self.x + self.Vx * self.dt
                self.y = self.y + self.Vy * self.dt
            else:
                self.x = self.x + self.Vmax * math.sin(self.alpha) * self.dt
                self.y = self.y + self.Vmax * math.cos(self.alpha) * self.dt
        if self.ka == True:
            self.alpha = self.alpha + self.omega * self.dt
        if self.kd == True:
            self.alpha = self.alpha - self.omega * self.dt
        if self.kshift == True:
            self.kshift = False

    def fire_torped(self, torp_arr, now_t):
        all_tubes_empty = True
        for i in range(0, len(self.torped_tubes)):
            if self.torped_tubes[i] - now_t >= self.recharge_time:
                all_tubes_empty = False
                self.torped_tubes[i] = now_t
                break
        if not(all_tubes_empty):
            torp = Torped(self.x, self.y, self.alpha, 10)
            torp_arr.append(torp)

