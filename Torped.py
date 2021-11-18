from math import *
import pygame

class Torped:

    def __init__(self, x, y, alpha, v):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.v = v
        self.dt = 0.1
        image = pygame.image.load('torpedo.png').convert_alpha()
        new_image_0 = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
        self.new_image = pygame.transform.rotate(new_image_0, (alpha - pi / 2) * 360 * (2 * pi)**-1)

    def moveTorped(self):
        self.x += self.v * sin(self.alpha) * self.dt
        self.y += self.v * cos(self.alpha) * self.dt
        pass

    def Hit(self):
        return True

    def detonation(self):
        print("Фюрер передает Привет!")
        pass


