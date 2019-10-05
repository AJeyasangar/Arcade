#This program is used to make sure that the paddles dont got out of the screen. It is also used to check if the ball touches the wall on the left or right which means that the player has lost the game. If the ball touches the top or bottom part of the screem it should make the ball to bounce.

import pygame


class Ball:
    def __init__(self, screen, pos_x, pos_y, score_left, score_right):
        self.speed_x = 10
        self.speed_y = 10
        self.screen = screen
        pos_x = pos_x + self.speed_x
        if pos_x > 640:
            if pos_y > (0.5 * 480):
                self.speed_y = 10
            else:
                self.speed_y = -10
            pos_x = int(0.5 * 640)
            pos_y = int(0.5 * 480)
            score_left += 1
        elif pos_x < 0:
            if pos_y > (0.5 * 480):
                self.speed_y = 10
            else:
                self.speed_y = -10
            pos_x = int(0.5 * 640)
            pos_y = int(0.5 * 480)
            score_right += 1
        print("1", pos_y)
        pos_y += self.speed_y
        print("2", pos_y)
        if pos_y > 480:
            self.speed_y = -10
        elif pos_y < 0:
            self.speed_y = 10
        print("3", pos_y)
        pygame.draw.circle(self.screen, (255, 255, 255), [pos_x, pos_y], 10)
