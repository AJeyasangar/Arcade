import pygame
import Platform_Scores
import Wall_Bounce
import Paddles
import Game_Controls
import pygame.math as Mathematics


class Process:
    def __init__(self, screen, width, height, val_y, val_y2):
        self.screen = screen
        self.val_y = val_y
        self.val_y2 = val_y2
        self.clock = pygame.time.Clock()
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height

    def Pong_Function(self, left, right, ball_pos, score_left, score_right, ball_speed,
                speed_direction, speed_increase, speed_val, last_ball_pos):
        right += self.val_y
        left += self.val_y2
        self.screen.fill((0, 0, 0))
        Platform_Scores.Screen(self.screen, self.width, score_left, score_right).score_board()
        result = Paddles.Paddles(self.screen, right, left, ball_pos, ball_speed,
                                 speed_direction, speed_val, speed_increase, last_ball_pos).hit()

        ball_pos = result[0]
        ball_speed = result[1]
        speed_direction = result[2]
        speed_val = result[3]
        ball_pos = ball_pos + ball_speed
        result = Wall_Bounce.BounceBoundaries(ball_pos, ball_speed, self.width, self.height,
                                              speed_val, last_ball_pos).check(score_left, score_right, speed_direction)
        ball_pos = result[0]

        ball_speed = result[1]
        score_left = result[2]
        score_right = result[3]
        speed_direction = result[4]
        speed_val = result[5]
        last_ball_pos = result[6]
        ball_pos += ball_speed
        print(ball_pos)
        pygame.draw.circle(self.screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), 7)
        print(self.clock.tick(30))
        pygame.display.flip()

        return ball_pos, speed_val, speed_direction, ball_speed, score_left, score_right
