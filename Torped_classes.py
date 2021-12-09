import os
import sys
from math import *
import pygame


class Torped:

    def __init__(self, x, y, alpha, v):
        self.k = 1
        self.hit = False
        self.hit_time = 0
        self.x = x
        self.y = y
        self.alpha = alpha
        self.v = v
        self.dt = 0.1
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        image = pygame.image.load(path + '/torpedo.png').convert_alpha()
        new_image_0 = pygame.transform.scale(image, (int(image.get_width() * 0.05), int(image.get_height() * 0.05)))
        self.new_image = pygame.transform.rotate(new_image_0, (alpha - pi) * 360 * (2 * pi) ** -1)

    def moveTorped(self):
        self.x += self.v * sin(self.alpha - pi / 2) * self.dt
        self.y += self.v * cos(self.alpha - pi / 2) * self.dt
        pass





