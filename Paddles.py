import pygame
import pygame.math as Mathematics
import maths


class Paddles:
    def __init__(self, screen, right, left, ball_pos, ball_speed, speed_direction, speed_val, speed_increase, last_ball_pos):
        self.right = right
        self.left = left
        self.ball_pos = ball_pos
        self.ball_speed = ball_speed
        self.speed_direction = speed_direction
        self.speed_increase = speed_increase
        pygame.draw.rect(screen, (255, 255, 255), (right[0], right[1], 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (left[0], left[1], 10, 100))
        self.angle = maths.Angle(self.ball_pos, self.ball_speed, self.speed_direction).calculate
        self.speed_val = speed_val

    def hit(self):
        if self.ball_pos[0] <= 12 and int(self.left[1]) <= self.ball_pos[1] <= (int(self.left[1] + 100)):
            self.ball_pos[0] = 12
            if self.ball_pos[1] == self.left[1]:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(- self.angle)
            elif self.ball_pos[1] >= self.left[1]:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(-(self.angle * 2) - 15)
            else:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate((self.angle * 2) + 15)
            if self.speed_val < 10:
                self.speed_val += self.speed_increase
            self.speed_direction = True
        elif self.ball_pos[0] >= 1188 and int(self.right[1]) <= self.ball_pos[1] <= (int(self.right[1] + 100)):
            self.ball_pos[0] = 1188
            if self.ball_pos[1] == self.left[1]:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(-self.angle)
            elif self.ball_pos[1] >= self.left[1]:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate((self.angle * 2) + 15)
            else:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(-(self.angle * 2) - 15)
            self.speed_direction = False
            if self.speed_val < 10:
                self.speed_val += self.speed_increase
        return self.ball_pos, self.ball_speed, self.speed_direction, self.speed_val

