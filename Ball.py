# This is the function for the balls movements. It contains the maths to predict the angle of rebound.
import pygame


class Ball:
    def __init__(self, screen, ball_pos ):
        pygame.draw.circle(screen, (255, 255, 255), (ball_pos), 10)
        print(ball_pos)

    def ballangles(self):
        pass