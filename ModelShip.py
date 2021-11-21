import math
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
    def __init__(self, m, b, x, y, alpha, V, gameXP, color, F, TF, dt, quantity_of_torpeds, recharge_time, maxXP):
        self.maxXP = maxXP
        self.m = choice(MASS)
        self.b = 0.01
        self.x = 450
        self.y = 20
        self.alpha = 0
        self.V = 100
        self.gameXP = maxXP/2
        self.color = choice(COLOR)
        self.F = choice(FORCE)
        self.TF = choice(TURNFORCE)
        self.dt = 0.1
        # Количество торпедных аппаратов у данного корабля и время их перезарядки
        self.quantity_of_torpeds = quantity_of_torpeds
        self.recharge_time = recharge_time
        # создание массива в котором хранится время последнего заряжания этого i-го торпедного аппарата
        self.torped_tubes = []
        for i in range(0, self.quantity_of_torpeds):
            self.torped_tubes.append(300*60)
        # это сделано Сомом для отображения


    def MoveForward(self,alpha, screen):
        image_1 = pygame.image.load('/torpedo-bombers/Bismark_top-removebg-preview.png')
        new_image_0 = pygame.transform.scale(image_1, (int(image_1.get_width() * 0.5), int(image_1.get_height() * 0.5)))
        self.new_image = pygame.transform.rotate(new_image_0, (alpha + math.pi / 2) * 360 * (2 * math.pi) ** -1)
        screen.blit(self.new_image, (self.x, self.y))
        self.x += (self.F / self.b - (self.F / self.b - self.V * math.sin(self.alpha)) * math.exp((-self.b / self.m) * 0.5)) * self.dt
        pass






