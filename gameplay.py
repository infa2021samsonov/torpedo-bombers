from Torped import *


class Gameplay:
    def __init__(self):
        self.torpeds = [Torped]

    def drawShips(self):
        pass

    def drawInfo(self):
        pass

    def drawTime(self):
        pass

    def drawTorpeds(self,screen):
        for i in self.torpeds:
            if (i.x <= 1600) and (i.x >= 0) and (i.y <= 900) and (i.y >= 0):
                i.moveTorped()
                if i.Hit():
                    i.detonation()
                    self.torpeds.remove(i)
                else:
                    screen.draw
            else:
                self.torpeds.remove(i)

        pass
