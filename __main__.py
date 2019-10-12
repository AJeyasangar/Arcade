#This links all the programs together so the program can work
import Game_Controls
import pygame
import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1200
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

    def __call__(self):
        #menu = Menu.Menu(self.screen, self.width, self.height).draw()
        self.screen.fill((0, 0, 0))
        Game_Controls.Game(self.screen, self.width, self.height).event_process



if __name__ == '__main__':
    game = Game()
    game()
