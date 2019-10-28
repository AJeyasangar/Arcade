import pygame


class Screen:
    def __init__(self, info):
        self.width = info.width
        self.score_left = info.score_left
        self.score_right = info.score_right
        self.font = pygame.font.Font("arcade.ttf",  34)
        self.screen = info.screen

    def score_board(self):
        scores = self.font.render("%2s:%2s" % (str(self.score_left), str(self.score_right)), 1, (255, 255, 255))
        text_pos = scores.get_rect(centerx=self.width / 2)
        self.screen.blit(scores, text_pos)
