import math
import os
import sys
from Torped_classes import *
from random import choice
from random import randint
import pygame
from pygame.draw import *

FPS = 30

StartXP = [100, 200, 300]

RED = 0xFF0000
GREEN = 0x00FF00
COLOR = [RED, GREEN]
FORCE = [100, 200, 300]
TURNFORCE = [10, 20, 30]
MASS = [1000, 2000, 3000]


class GameShipLeft:
    def __init__(self, name, m, b, x, y, alpha, Vmax, Vmaxback, Vxmax, Vymax, Vx, Vy, a, omega, gameXP, color, F, TF,
                 dt, maxXP,
                 quantity_of_torpeds, recharge_time):
        self.name = 'IOWA'
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.image = pygame.image.load(path + '/' + self.name + '_top-removebg-preview.png').convert_alpha()
        self.new_image_0 = pygame.transform.scale(self.image, (
        int(self.image.get_width() * 0.15), int(self.image.get_height() * 0.15)))
        self.height = self.new_image_0.get_height()
        self.width = self.new_image_0.get_width()
        self.maxXP = maxXP
        self.m = choice(MASS)
        self.b = 0.01
        self.x = 100
        self.y = 800
        self.alpha = 0
        self.Vx = 0
        self.Vy = 0
        self.Vmax = 5
        self.Vmaxback = 5
        self.Vxmax = 50
        self.Vymax = 50
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
        self.klshift = False
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
                self.klshift = True

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
                self.klshift = False

    def DrawShip(self, screen):
        self.new_image = pygame.transform.rotate(self.new_image_0, (self.alpha + pi / 2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x - self.new_image.get_width() / 2, self.y - self.new_image.get_height() / 2))
        pass

    def same_orientation(self):
        x1 = -sin(self.alpha)
        y1 = -cos(self.alpha)
        x2 = self.Vx
        y2 = self.Vy
        return x1 * x2 + y1 * y2 <= 0

    def Move(self, torp_arr):
        self.x = self.x - self.Vx * self.dt
        self.y = self.y - self.Vy * self.dt
        if (self.same_orientation() == False) or (
                (self.same_orientation() == True) and (self.Vx ** 2 + self.Vy ** 2 < self.Vmax ** 2)):
            if self.kw == True:
                self.Vx = self.Vx + self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.Vy + self.a * math.cos(self.alpha) * self.dt
        if (self.same_orientation() == True) or (
                (self.same_orientation() == False) and (self.Vx ** 2 + self.Vy ** 2 < self.Vmaxback ** 2)):
            if self.ks == True:
                self.Vx = self.Vx - self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.Vy - self.a * math.cos(self.alpha) * self.dt

        if (self.ka == True):
            self.omega = math.sqrt(math.sqrt(self.Vx ** 2 + self.Vy ** 2)/self.Vmax)*0.05
            self.alpha = self.alpha + self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if (self.kd == True):
            self.omega = math.sqrt(math.sqrt(self.Vx ** 2 + self.Vy ** 2) / self.Vmax) * 0.05
            self.alpha = self.alpha - self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(- self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(- self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if self.klshift == True:
            self.klshift = False

    def fire_torped(self, torp_arr, now_t, k):
        h = 40
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        all_tubes_empty = True
        for i in range(0, len(self.torped_tubes)):
            if self.torped_tubes[i] - now_t >= self.recharge_time:
                all_tubes_empty = False
                self.torped_tubes[i] = now_t
                break
        if not (all_tubes_empty):
            pygame.mixer.music.load(path + "/fire.mp3")
            pygame.mixer.music.play()
            torp = Torped(self.x + k * h * math.cos(self.alpha), self.y - k * h * math.sin(self.alpha), self.alpha + pi * (k < 0), 20)
            torp_arr.append(torp)

    def collision(self, torpedo):
        h = self.height / 2

        w = self.width / 2
        a = -self.alpha
        fx1 = self.x + w * sin(a)
        fy1 = self.y - w * cos(a)
        fx2 = self.x - w * sin(a)
        fy2 = self.y + w * cos(a)
        gx1 = self.x - h * cos(a)
        gy1 = self.y - h * sin(a)
        gx2 = self.x + h * cos(a)
        gy2 = self.y + h * sin(a)
        A1 = fy1 - fy2
        B1 = fx2 - fx1
        C1 = fy2 * fx1 - fx2 * fy1

        A2 = gy1 - gy2
        B2 = gx2 - gx1
        C2 = gy2 * gx1 - gx2 * gy1
        Ro1 = abs(A1 * torpedo.x + B1 * torpedo.y + C1) / sqrt(A1 ** 2 + B1 ** 2)
        Ro2 = abs(A2 * torpedo.x + B2 * torpedo.y + C2) / sqrt(A2 ** 2 + B2 ** 2)
        ans = False
        if (Ro1 <= h) and (Ro2 <= w):
            ans = True
        return ans


class GameShipRight:
    def __init__(self, name, m, b, x, y, alpha, Vmax, Vmaxback, Vxmax, Vymax, Vx, Vy, a, omega, gameXP, color, F, TF,
                 dt, maxXP,
                 quantity_of_torpeds, recharge_time):
        self.name = 'IOWA'
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.image = pygame.image.load(path + '/' + self.name + '_top-removebg-preview.png').convert_alpha()
        self.new_image_0 = pygame.transform.scale(self.image, (
        int(self.image.get_width() * 0.15), int(self.image.get_height() * 0.15)))
        self.height = self.new_image_0.get_height()
        self.width = self.new_image_0.get_width()
        self.maxXP = maxXP
        self.m = choice(MASS)
        self.b = 0.01
        self.x = 1500
        self.y = 800
        self.alpha = 0
        self.Vx = 0
        self.Vy = 0
        self.Vmax = 5
        self.Vmaxback = 5
        self.Vxmax = 50
        self.Vymax = 50
        self.a = 5
        self.omega = 0.1
        self.gameXP = maxXP / 2
        self.color = choice(COLOR)
        self.F = choice(FORCE)
        self.TF = choice(TURNFORCE)
        self.dt = 0.1
        self.ki = False
        self.kk = False
        self.kj = False
        self.kl = False
        self.krshift = False
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

            if event.key == pygame.K_i:
                self.ki = True
            if event.key == pygame.K_k:
                self.kk = True
            if event.key == pygame.K_j:
                self.kj = True
            if event.key == pygame.K_l:
                self.kl = True
            if event.key == pygame.K_RSHIFT:
                self.krshift = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                self.ki = False
            if event.key == pygame.K_k:
                self.kk = False
            if event.key == pygame.K_j:
                self.kj = False
            if event.key == pygame.K_l:
                self.kl = False
            if event.key == pygame.K_RSHIFT:
                self.krshift = False

    def DrawShip(self, screen):
        self.new_image = pygame.transform.rotate(self.new_image_0, (self.alpha + pi / 2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x - self.new_image.get_width() / 2, self.y - self.new_image.get_height() / 2))
        pass

    def same_orientation(self):
        x1 = -sin(self.alpha)
        y1 = -cos(self.alpha)
        x2 = self.Vx
        y2 = self.Vy
        return x1 * x2 + y1 * y2 <= 0

    def Move(self, torp_arr):
        self.x = self.x - self.Vx * self.dt
        self.y = self.y - self.Vy * self.dt
        if (self.same_orientation() == False) or (
                (self.same_orientation() == True) and (self.Vx ** 2 + self.Vy ** 2 < self.Vmax ** 2)):
            if self.ki == True:
                self.Vx = self.Vx + self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.Vy + self.a * math.cos(self.alpha) * self.dt
        if (self.same_orientation() == True) or (
                (self.same_orientation() == False) and (self.Vx ** 2 + self.Vy ** 2 < self.Vmaxback ** 2)):
            if self.kk == True:
                self.Vx = self.Vx - self.a * math.sin(self.alpha) * self.dt
                self.Vy = self.Vy - self.a * math.cos(self.alpha) * self.dt

        if (self.kj == True):
            self.omega = math.sqrt(math.sqrt(self.Vx ** 2 + self.Vy ** 2) / self.Vmax) * 0.05
            self.alpha = self.alpha + self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if (self.kl == True):
            self.omega = math.sqrt(math.sqrt(self.Vx ** 2 + self.Vy ** 2) / self.Vmax) * 0.05
            self.alpha = self.alpha - self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(- self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(- self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if self.krshift == True:
            self.krshift = False

    def fire_torped(self, torp_arr, now_t, k):
        h = 40
        path = os.path.abspath(os.path.dirname(sys.argv[0]))

        all_tubes_empty = True
        for i in range(0, len(self.torped_tubes)):
            if self.torped_tubes[i] - now_t >= self.recharge_time:
                all_tubes_empty = False
                self.torped_tubes[i] = now_t
                break
        if not (all_tubes_empty):
            pygame.mixer.music.load(path + "/fire.mp3")
            pygame.mixer.music.play()
            torp = Torped(self.x + k * h * math.cos(self.alpha), self.y - k * h * math.sin(self.alpha), self.alpha + pi * (k < 0), 20)
            torp_arr.append(torp)

    def collision(self, torpedo):
        h = self.height / 2

        w = self.width / 2
        a = -self.alpha
        fx1 = self.x + w * sin(a)
        fy1 = self.y - w * cos(a)
        fx2 = self.x - w * sin(a)
        fy2 = self.y + w * cos(a)
        gx1 = self.x - h * cos(a)
        gy1 = self.y - h * sin(a)
        gx2 = self.x + h * cos(a)
        gy2 = self.y + h * sin(a)
        A1 = fy1 - fy2
        B1 = fx2 - fx1
        C1 = fy2 * fx1 - fx2 * fy1

        A2 = gy1 - gy2
        B2 = gx2 - gx1
        C2 = gy2 * gx1 - gx2 * gy1
        Ro1 = abs(A1 * torpedo.x + B1 * torpedo.y + C1) / sqrt(A1 ** 2 + B1 ** 2)
        Ro2 = abs(A2 * torpedo.x + B2 * torpedo.y + C2) / sqrt(A2 ** 2 + B2 ** 2)
        ans = False
        if (Ro1 <= h) and (Ro2 <= w):
            ans = True
        return ans


class Ship():
    def __init__(self, name, x, y, alpha, Vmax, Vmaxback, Vx, Vy, a, omega, maxXP, quantity_of_torpeds, recharge_time):
        self.name = name
        self.x = x
        self.y = y
        self.maxXP = maxXP
        self.alpha = alpha
        self.Vx = Vx
        self.Vy = Vy
        self.Vmax = Vmax
        self.Vmaxback = Vmaxback
        self.a = a
        self.omega = omega
        self.quantity_of_torpeds = quantity_of_torpeds
        self.recharge_time = recharge_time
