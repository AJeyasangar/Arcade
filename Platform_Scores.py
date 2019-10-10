import pygame


class Screen:
    def __init__(self, screen, width, score_left, score_right):
        self.width = width
        self.score_left = score_left
        self.score_right = score_right
        self.font = pygame.font.Font(None,  34)
        self.screen = screen

    def arena(self):
        pass

    def score_board(self):
        scores = self.font.render("%2s:%2s" % (str(self.score_left), str(self.score_right)), 1, (255, 255, 255))
        text_pos = scores.get_rect(centerx=self.width / 2)
        self.screen.blit(scores, text_pos)
