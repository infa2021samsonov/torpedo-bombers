import os
import sys

import pygame
class Game_res:

    def __init__(self, winner_name, win_game):
        self.winner_name = winner_name
        self.font = pygame.font.SysFont('Rockwell', 80)
        self.win_game = win_game

    def draw(self, screen):
        label = ""
        if self.win_game:
            label = self.font.render(self.winner_name + " IS WINNER!", True, (212, 175, 55), None)
        else:
            label = self.font.render("DRAW", True, (212, 175, 55), None)
        screen.blit(label, (800 - label.get_width()/2, 300 + label.get_height()/2))

def play_win_music():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    pygame.mixer.music.load(path + "/winmus.mp3")
    pygame.mixer.music.play()