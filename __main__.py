#This links all the programs together so the program can work
import Game_Controls
import pygame


class Game:
    def __init__(self):
        pygame.init()
        width = 1200
        height = 600
        self.screen = pygame.display.set_mode((width, height))
        Game_Controls.Game(self.screen, width, height).event_process()


if __name__ == '__main__':
    Game()
