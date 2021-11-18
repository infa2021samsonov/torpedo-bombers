import math


class Torped:

    def __init__(self, x, y, alpha, v):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.v = v
        self.vx = v*math.sin(alpha)
        self.vy = x*math.cos(alpha)
        self.dt = 0.1

    def moveTorped(self):
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        pass

    def Hit(self):
        return True

    def detonation(self):
        print("Фюрер передает Привет!")
        pass


