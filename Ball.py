# This is the function for the balls movements. It contains the maths to predict the angle of rebound.
import pygame


class Ball:
    def __init__(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (50, 50), 10)

    def ballangles(self):
        pass