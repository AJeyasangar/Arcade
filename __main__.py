#This links all the programs together so the program can work
import Game_Controls
import pygame
import Ball
import Paddles


class Game:
    def __init__(self):
        pygame.init()
        global screen
        screen = pygame.display.set_mode((1200, 600))
        crashed = False

        while not crashed:
            Paddle_Pos = Game_Controls.Game(screen).event_process()


Game()




