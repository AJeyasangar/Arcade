# This is the function for the balls movements. It contains the maths to predict the angle of rebound.
import pygame, BounceBall


class Ball:
    def __init__(self, screen, pos_x, pos_y, speed_x, speed_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.score_left = 0
        self.score_right = 0
        self.screen = screen
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.pos_x = self.pos_x + self.speed_x
        self.pos_y = self.pos_y + self.speed_y
        if self.pos_x > 640:
            if self.pos_y > 240:
                self.speed_y = abs(self.speed_y)
            else:
                self.speed_y = -abs(self.speed_y)
            self.pos_x = int(0.5 * 640)
            self.pos_y = int(0.5 * 480)
            self.score_left += 1
        elif self.pos_x < 0:
            if self.pos_y > 240:
                self.speed_y = abs(self.speed_y)
            else:
                self.speed_y = -abs(self.speed_y)
            self.pos_x = int(0.5 * 640)
            self.pos_y = int(0.5 * 480)
            self.score_right += 1

        if self.pos_y > 480:
            self.speed_y = -self.speed_y
        elif self.pos_y < 0:
            self.speed_y = abs(self.speed_y)
        pygame.draw.circle(self.screen, (255, 255, 255), [self.pos_x, self.pos_y], 10)


