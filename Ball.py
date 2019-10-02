# This is the function for the balls movements. It contains the maths to predict the angle of rebound.
import pygame


class Ball:
    def __init__(self, screen, ball_pos ):
        self.screen = screen
        self.ball_pos = ball_pos
        self.hitbox = (self. ball_pos[0] -10, self.ball_pos[1]- 10, 20, 20)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), self.ball_pos, 10)
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
