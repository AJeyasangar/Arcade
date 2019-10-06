import pygame


class Paddles:
    def __init__(self, screen, right, left):
        pygame.draw.rect(screen, (255, 255, 255), (right[0], right[1], 10, 100))
        print(right)
        pygame.draw.rect(screen, (255, 255, 255), (left[0], left[1], 10, 100))
        print(left)
        self.left = left
        self.right = right

    def hit(self, pos_x, pos_y, speed_x):
        if pos_x <= (10) and pos_y >= int(0.5 * 600 - 0.5 * 100) and pos_y <= (int(0.5 * 600 - 0.5 * 100) + 10):
            pos_x = 10
            speed_x = abs(speed_x)
        elif pos_x >= 1190 and pos_y >= int(0.5 * 600 - 0.5 * 100) and pos_y <= (int(0.5 * 600 - 0.5 * 100) + 100):
            pos_x = 1190
            speed_x = -speed_x
        return pos_x, speed_x

