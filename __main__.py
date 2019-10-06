#This links all the programs together so the program can work
import Game_Controls
import pygame


class Game:
    def __init__(self):
        pygame.init()
        width = 1200
        height = 600
        self.screen = pygame.display.set_mode((width, height))
        crashed = False

        self.speed_x = 3
        self.speed_y = 3
        self.score_left = 0
        self.score_right = 0


        Paddle_Pos = Game_Controls.Game(self.screen).event_process()


Game()
