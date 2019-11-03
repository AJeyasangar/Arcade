import pygame
import pygame.math as Mathematics


class BounceBoundaries:
    def __init__(self, info):
        self.ball_pos = info.ball_pos
        self.ball_speed = info.ball_speed
        self.width = info.width
        self.height = info.height
        self.speed_val = info.speed_val
        self.last_ball_pos = info.last_ball_pos

    def check(self, info):
        if self.ball_pos[0] > self.width:
            if self.ball_pos[1] > (0.5 * self.height):
                self.ball_speed = Mathematics.Vector2(-self.speed_val).rotate(90)
            else:
                self.ball_speed = Mathematics.Vector2(-self.speed_val).rotate(90)

            self.ball_pos = Mathematics.Vector2(int(0.5 * self.width), int(0.5 * self.height))
            info.score_left += 1
            self.speed_val = 5
            info.speed_direction = True
        elif self.ball_pos[0] < 0:
            if self.ball_pos[1] > (0.5 * self.height):
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(90)
            else:
                self.ball_speed = Mathematics.Vector2(5)
            self.ball_pos = Mathematics.Vector2(int(0.5 * self.width), int(0.5 * self.height))
            info.score_right += 1
            self.speed_val = 5
            info.speed_direction = False
        if self.ball_pos[1] >= self.height - 3.5:
            if info.speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(-90)
            elif not info.speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(180)
            self.last_ball_pos = 0
            info.last_bounce = self.ball_pos
        elif self.ball_pos[1] < 3.5:
            if info.speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(0)
            elif not info.speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(90)
            self.last_ball_pos = self.height
            info.last_bounce = self.ball_pos
        return self.ball_pos, self.ball_speed, info.score_left, info.score_right, info.speed_direction, self.speed_val, \
               self.last_ball_pos, info.last_bounce
