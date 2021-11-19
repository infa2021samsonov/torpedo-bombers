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


class GameShip:
    def _init_(self):
        #self.m = choice(MASS)
        self.x = 450
        self.y = 20
        self.alpha = 0
        self.V = 0
        self.gameXP = choice(StartXP)
        self.color = choice(COLOR)
        self.F = choice(FORCE)
        self.TF = choice(TURNFORCE)



