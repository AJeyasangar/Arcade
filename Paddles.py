import pygame


class Paddles:
    def __init__(self, screen, right, left, pos_x, pos_y, speed_x):
        pygame.draw.rect(screen, (255, 255, 255), (right[0], right[1], 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (left[0], left[1], 10, 100))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x= speed_x
        self.left = left
        self.right = right

    def hit(self):
        if self.pos_x <= (22) and self.pos_y >= int(0.5 * 480 - 0.5 * 100) and self.pos_y <= (int(0.5 * 480 - 0.5 * 100) + 10):
            self.pos_x = 22
            self.speed_x = abs(self.speed_x)
        elif self.pos_x >= 618 and self.pos_y >= int(0.5 * 480 - 0.5 * 100) and self.pos_y <= (int(0.5 * 480 - 0.5 * 100) + 100):
            self.pos_x = 618
            self.speed_x = -self.speed_x
        return self.speed_x

