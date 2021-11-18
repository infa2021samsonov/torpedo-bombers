from Torped import *
import pygame

class Gameplay:
    def __init__(self):
        self.torpeds = [Torped]

    def drawShips(self):
        pass

    def drawInfo(self):

        pass

    def drawTime(self, screen):
        pass

    def drawTorpeds(self,screen):
        for i in self.torpeds:
            if (i.x <= 1600) and (i.x >= 0) and (i.y <= 900) and (i.y >= 0):
                i.moveTorped()
                if i.Hit():
                    i.detonation()
                    self.torpeds.remove(i)
                else:
                    screen.blit(i.new_image, (i.x, i.y))
            else:
                self.torpeds.remove(i)
