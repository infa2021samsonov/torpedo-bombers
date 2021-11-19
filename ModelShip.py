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
    def __init__(self, m, x, y, alpha, V, gameXP, color, F, TF, dt):
        self.m = choice(MASS)
        self.x = 450
        self.y = 20
        self.alpha = 0
        self.V = 0
        self.gameXP = choice(StartXP)
        self.color = choice(COLOR)
        self.F = choice(FORCE)
        self.TF = choice(TURNFORCE)
        self.dt = 0.1
        image = pygame.image.load('Bismark_top-removebg-preview.png').convert_alpha()
        new_image_0 = pygame.transform.scale(image, (image.get_width() * 0.5, image.get_height() * 0.5))
        self.new_image = pygame.transform.rotate(new_image_0, (alpha + pi/2) * 360 * (2 * pi) ** -1)



    def Move(self, m, x, y, alpha, V, gameXP, color, F, TF):
        self.x += (F / b - (F / b - self.V * sin(self.alpha)) * exp((-b / m) * (t - t0))) * self.dt
        self.y += (self.V * cos(self.alpha)  - (TF / m) * (t - t0)) * self.dt
        pass