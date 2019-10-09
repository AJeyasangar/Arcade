import pygame


class Screen:
    def __init__(self,screen, width, score_left, score_right):
        self.width = width
        self.score_left = score_left
        self.score_right = score_right
        self.font = pygame.font.Font(None,  34)
        self.screen = screen

    def arena(self):
        pass

    def score_board(self):
        Scores = self.font.render("%2s:%2s" % (str(self.score_left), str(self.score_right)), 1, (255, 255, 255))
        textpos = Scores.get_rect(centerx=self.width / 2)
        print("here")
        self.screen.blit(Scores, textpos)

