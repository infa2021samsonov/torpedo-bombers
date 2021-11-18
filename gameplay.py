from Torped import *
import pygame


class Gameplay:
    def __init__(self):
        self.torpeds = [Torped]
        self.time = 300
        pygame.font.init()
        self.font1 = pygame.font.SysFont('Rockwell', 60)
        self.font2 = pygame.font.SysFont('Rockwell', 80)

    def drawShips(self, screen):
        pass

    def drawInfo(self, screen):
        red_name_lable = self.font2.render("Red", True, (204, 0, 0), None)
        screen.blit(red_name_lable, (30,30))
        green_name_lable = self.font2.render("Green", True, (51, 102, 0), None)
        screen.blit(green_name_lable, (1315, 30))

    def drawTime(self, screen):
        seconds = str(self.time % 60)
        if seconds == '0':
            seconds = '00'
        time_label = self.font1.render(str(self.time // 60) + ":" + seconds, True, (255, 255, 255), None)
        screen.blit(time_label, (750, 30))
        pass

    def drawTorpeds(self, screen):
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
