import pygame


class Paddles:
    def __init__(self, screen, pos):
        self.pos = pos
        pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], 10, 100))

    def paddle_boundaries(self):
        y = [self.pos[1]-50, self.pos[1] + 50]
        print(y)


