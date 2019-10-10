import pygame, random


class Paddles:
    def __init__(self, screen, right, left):
        self.right = right
        self.left = left
        pygame.draw.rect(screen, (255, 255, 255), (right[0], right[1], 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (left[0], left[1], 10, 100))

    def hit(self, pos_x, pos_y, speed_x):
        if pos_x <= 12 and int(self.left[1]) <= pos_y <= (int(self.left[1] + 100)):
            speed_x = random.randint(10, 15)
            pos_x = 12
            speed_x = abs(speed_x)
        elif pos_x >= 1188 and int(self.right[1]) <= pos_y <= (int(self.right[1] + 100)):
            speed_x = random.randint(10, 15)
            pos_x = 1188
            speed_x = -abs(speed_x)
        return pos_x, speed_x

    def ai_paddle(self, ball_x_pos, ball_y_pos, speed_x, speed_y):
        if speed_x > 0:
            x_difference = 1188 - ball_x_pos
            loop = x_difference // speed_x
            paddle_y_pos = ball_y_pos + (loop*speed_y)
            paddle_y_pos -= 50
        return paddle_y_pos


