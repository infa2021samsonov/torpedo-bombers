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
    def __init__(self, name, m, b, x, y, alpha, Vmax, Vxmax, Vymax, Vx, Vy, a, omega, gameXP, color, F, TF, dt, maxXP,
                 quantity_of_torpeds, recharge_time):
        self.name = 'IOWA'
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        image = pygame.image.load(path + '/'+self.name + '_top-removebg-preview.png').convert_alpha()
        self.new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.15), int(image.get_height() * 0.15)))
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
        self.Vmax = 70.7
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
        self.new_image = pygame.transform.rotate(self.new_image_0, (self.alpha + pi/2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x - self.new_image.get_width()/2, self.y - self.new_image.get_height()/2))
        circle(screen, (255,0,0), (self.x, self.y), 10)
        pass




    def Move(self, torp_arr):
        self.x = self.x - self.Vx * self.dt
        self.y = self.y - self.Vy * self.dt
        if self.kw == True:
            self.Vx = self.Vx + self.a * math.sin(self.alpha) * self.dt
            self.Vy = self.Vy + self.a * math.cos(self.alpha) * self.dt
        if self.ks == True:
            self.Vx = self.Vx - self.a * math.sin(self.alpha) * self.dt
            self.Vy = self.Vy - self.a * math.cos(self.alpha) * self.dt


        if ((self.ka == True) and ((self.Vx**2 + self.Vy**2) > 10)):

            self.alpha = self.alpha + self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(self.omega * self.dt)
            self.Vy =  - self.Vx * math.sin(self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if ((self.kd == True) and ((self.Vx**2 + self.Vy**2) > 10)):

            self.alpha = self.alpha - self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin( - self.omega * self.dt)
            self.Vy = - self.Vx * math.sin( - self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if self.klshift == True:
            self.klshift = False


    def fire_torped(self, torp_arr, now_t):
        h = 10
        path = os.path.abspath(os.path.dirname(sys.argv[0]))

        all_tubes_empty = True
        for i in range(0, len(self.torped_tubes)):
            if self.torped_tubes[i] - now_t >= self.recharge_time:
                all_tubes_empty = False
                self.torped_tubes[i] = now_t
                break
        if not(all_tubes_empty):
            pygame.mixer.music.load(path + "/fire.mp3")
            pygame.mixer.music.play()
            torp = Torped(self.x + h*math.cos(self.alpha), self.y + h*math.sin(self.alpha), self.alpha, 10)
            torp_arr.append(torp)





    def collision(self,torpedo):
        A1 = - self.height
        B1 = - self.width
        C1 = self.x * self.height + self.y * self.width
        A2 = self.height
        B2 = self.width
        C2 = - self.x * self.height + self.y * self.width
        Ro1 = abs(A1 * torpedo.x + B1 * torpedo.y + C1)/sqrt(A1**2 + B1**2 + C1**2)
        Ro2 = abs(A2 * torpedo.x + B2 * torpedo.y + C2) / sqrt(A2 ** 2 + B2 ** 2 + C2 ** 2)
        answer = False
        if (Ro1 <= 21 / 2) and (Ro2 <= 156 / 2):
            answer = True
        return answer


class GameShipRight:
    def __init__(self, name, m, b, x, y, alpha, Vmax, Vxmax, Vymax, Vx, Vy, a, omega, gameXP, color, F, TF, dt, maxXP,
                 quantity_of_torpeds, recharge_time):
        self.name = 'IOWA'
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        image = pygame.image.load(path + '/'+self.name + '_top-removebg-preview.png').convert_alpha()
        self.new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.15), int(image.get_height() * 0.15)))
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
        self.Vmax = 70.7
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
        self.new_image = pygame.transform.rotate(self.new_image_0, (self.alpha + pi/2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x - self.new_image.get_width()/2, self.y - self.new_image.get_height()/2))
        circle(screen, (255,0,0), (self.x, self.y), 10)
        pass

    def Move(self, torp_arr):
        self.x = self.x - self.Vx * self.dt
        self.y = self.y - self.Vy * self.dt
        if self.ki == True:
            self.Vx = self.Vx + self.a * math.sin(self.alpha) * self.dt
            self.Vy = self.Vy + self.a * math.cos(self.alpha) * self.dt
        if self.kk == True:
            self.Vx = self.Vx - self.a * math.sin(self.alpha) * self.dt
            self.Vy = self.Vy - self.a * math.cos(self.alpha) * self.dt

        if ((self.kj == True) and ((self.Vx ** 2 + self.Vy ** 2) > 10)):
            self.alpha = self.alpha + self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if ((self.kl == True) and ((self.Vx ** 2 + self.Vy ** 2) > 10)):
            self.alpha = self.alpha - self.omega * self.dt
            self.Vx = self.Vx * math.cos(self.omega * self.dt) + self.Vy * math.sin(- self.omega * self.dt)
            self.Vy = - self.Vx * math.sin(- self.omega * self.dt) + self.Vy * math.cos(self.omega * self.dt)
        if self.krshift == True:
            self.krshift = False


    def fire_torped(self, torp_arr, now_t):
        h = 10
        path = os.path.abspath(os.path.dirname(sys.argv[0]))

        all_tubes_empty = True
        for i in range(0, len(self.torped_tubes)):
            if self.torped_tubes[i] - now_t >= self.recharge_time:
                all_tubes_empty = False
                self.torped_tubes[i] = now_t
                break
        if not(all_tubes_empty):
            pygame.mixer.music.load(path + "/fire.mp3")
            pygame.mixer.music.play()
            torp = Torped(self.x + h*math.cos(self.alpha), self.y + h*math.sin(self.alpha), self.alpha, 10)
            torp_arr.append(torp)





    def collision(self,torpedo):
        A1 = - self.height
        B1 = - self.width
        C1 = self.x * self.height + self.y * self.width
        A2 = self.height
        B2 = self.width
        C2 = - self.x * self.height + self.y * self.width
        Ro1 = abs(A1 * torpedo.x + B1 * torpedo.y + C1)/sqrt(A1**2 + B1**2 + C1**2)
        Ro2 = abs(A2 * torpedo.x + B2 * torpedo.y + C2) / sqrt(A2 ** 2 + B2 ** 2 + C2 ** 2)
        if (Ro1 <= 21 / 2) and (Ro2 <= 156 / 2):
            return True