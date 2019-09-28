import pygame


class Paddles:
    def __init__(self, screen, pos):
        pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], 10, 100))

    def paddle_boundaries(self):
        pass
