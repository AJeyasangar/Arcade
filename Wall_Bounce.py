import pygame
import pygame.math as Mathematics


class BounceBoundaries:
    def __init__(self, ball_pos, ball_speed, width, height, speed_val, last_ball_pos):
        self.ball_pos = ball_pos
        self.ball_speed = ball_speed
        self.width = width
        self.height = height
        self.speed_val = speed_val
        self.last_ball_pos = last_ball_pos

    def check(self, score_left, score_right, speed_direction):
        if self.ball_pos[0] > self.width:
            if self.ball_pos[1] > (0.5 * self.height):
                self.ball_speed = Mathematics.Vector2(-self.speed_val).rotate(90)
            else:
                self.ball_speed = Mathematics.Vector2(-self.speed_val).rotate(90)

            self.ball_pos = Mathematics.Vector2(int(0.5 * self.width), int(0.5 * self.height))
            score_left += 1
            self.speed_val = 5
            speed_direction = True
        elif self.ball_pos[0] < 0:
            if self.ball_pos[1] > (0.5 * self.height):
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(90)
            else:
                self.ball_speed = Mathematics.Vector2(5)
            self.ball_pos = Mathematics.Vector2(int(0.5 * self.width), int(0.5 * self.height))
            score_right += 1
            self.speed_val = 5
            speed_direction = False
        if self.ball_pos[1] >= self.height - 3.5:
            if speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(-90)
            elif not speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(180)
            self.last_ball_pos = 0
        elif self.ball_pos[1] < 3.5:
            if speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(0)
            elif not speed_direction:
                self.ball_speed = Mathematics.Vector2(self.speed_val).rotate(90)
            self.last_ball_pos = 600
        return self.ball_pos, self.ball_speed, score_left, score_right, speed_direction, self.speed_val, \
               self.last_ball_pos
