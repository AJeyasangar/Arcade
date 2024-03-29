import pygame
import pygame.math as Mathematics
import maths
from random import randint as rr


class Paddles:
    def __init__(self, info):
        self.right = info.right
        self.left = info.left
        self.ball_pos = info.ball_pos
        self.ball_speed = info.ball_speed
        self.speed_direction = info.speed_direction
        self.speed_increase = info.speed_increase
        self.width = info.width
        self.height = info.height
        pygame.draw.rect(info.screen, (255, 255, 255), (info.right[0], info.right[1], 10, 100))
        pygame.draw.rect(info.screen, (255, 255, 255), (info.left[0], info.left[1], 10, 100))
        self.angle = maths.Angle(self.ball_pos, self.ball_speed, self.speed_direction, info.last_bounce, self.width).calculate
        while self.angle > 80:
            self.angle -= 1
        self.speed_val = info.speed_val
        self.last_ball_pos = info.last_ball_pos

    def hit(self, info):
        print(self.angle)
        if self.ball_pos[0] <= 12 and int(self.left[1]) <= self.ball_pos[1] <= (int(self.left[1] + 100)):
            self.angle -= rr(10, 20)
            self.ball_pos[0] = 12
            self.ball_speed = Mathematics.Vector2(self.speed_val).rotate((270 - self.angle))
            if self.last_ball_pos == self.height:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(self.angle*2+180)
            if self.speed_val < 10:
                self.speed_val += self.speed_increase
            self.speed_direction = True
            info.last_bounce = self.ball_pos

        elif self.ball_pos[0] >= self.width-12 and int(self.right[1]) <= self.ball_pos[1] <= (int(self.right[1] + 100)):
            self.angle += rr(10, 20)
            self.ball_pos[0] = self.width-12
            self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(360 - (self.angle * 2))
            if self.last_ball_pos == self.height:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(self.angle)
            self.speed_direction = False
            if self.speed_val < 8:
                self.speed_val += self.speed_increase
            info.last_bounce = self.ball_pos
        return self.ball_pos, self.ball_speed, self.speed_direction, self.speed_val, info.last_bounce

