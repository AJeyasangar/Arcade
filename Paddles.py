import pygame


class Paddles:
    def __init__(self, screen, right, left):
        self.right = right
        self.left = left
        pygame.draw.rect(screen, (255, 255, 255), (right[0], right[1], 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (left[0], left[1], 10, 100))

    def hit(self, pos_x, pos_y, speed_x):
        if pos_x <= 12 and int(self.left[1]) <= pos_y <= (int(self.left[1] + 100)):
            pos_x = 12
            speed_x = abs(speed_x)
        elif pos_x >= 1188 and int(self.right[1]) <= pos_y <= (int(self.right[1] + 100)):
            pos_x = 1188
            speed_x = -abs(speed_x)
        return pos_x, speed_x

