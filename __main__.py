import Game_Controls
import pygame
import os


class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        _W,_H = pygame.display.Info().current_w, pygame.display.Info().current_h
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
        self.screen = pygame.display.set_mode((_W, _H), pygame.RESIZABLE)
        self.screen.fill((0, 0, 0))
        self.width = _W
        self.height = _H

    def __call__(self):
        Game_Controls.Game(self).event_process


if __name__ == '__main__':
    game = Game()
    game()
