import pygame
import Paddles
import BounceBall
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.left = [0, 100]
        self.right = [1190, 0]
        self.val_y = [0, 0]
        self.clock = pygame.time.Clock()
        self.speed = 5
        self.ball_x_pos = int(0.5 * 640)
        self.ball_y_pos = int(0.5 * 480)
        self.score_left = 0
        self.score_right = 0
        self.ball_x_speed = 3
        self.ball_y_speed = 3
        self.width = 1200
        self.height = 600

    def event_process(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.val_y[0] = -self.speed
                    if event.key == pygame.K_DOWN:
                        self.val_y[0] = self.speed
                    if event.key == pygame.K_w:
                        self.val_y[1] = -self.speed
                    if event.key == pygame.K_s:
                        self.val_y[1] = self.speed
                if event.type == pygame.KEYUP:
                    self.val_y[0] = 0
                    self.val_y[1] = 0
            self.right[1] += self.val_y[0]
            self.left[1] += self.val_y[1]
            self.screen.fill((0, 0, 0))

            self.ball_x_pos = self.ball_x_pos + self.ball_x_speed
            if self.ball_x_pos > self.width:
                if self.ball_y_pos > (0.5 * self.height):
                    self.ball_y_speed = abs(self.ball_y_speed)
                else:
                    self.ball_y_speed = -abs(self.ball_y_speed)
                self.ball_x_pos = int(0.5 * self.width)
                self.ball_y_pos = int(0.5 * self.height)
                self.score_left += 1
            elif self.ball_x_pos < 0:
                if self.ball_y_pos > (0.5 * self.height):
                    self.ball_y_speed = abs(self.ball_y_speed)
                else:
                    self.ball_y_speed = -abs(self.ball_y_speed)
                self.ball_x_pos = int(0.5 * self.width)
                self.ball_y_pos = int(0.5 * self.height)
                self.score_right += 1
            self.ball_y_pos = self.ball_y_pos + self.ball_y_speed
            if self.ball_y_pos > self.height:
                self.ball_y_speed = -self.ball_y_speed
            elif self.ball_y_pos < 0:
                self.ball_y_speed = abs(self.ball_y_speed)
            pygame.draw.circle(self.screen, (255, 255, 255), [self.ball_x_pos, self.ball_y_pos], 10)
            result = Paddles.Paddles(self.screen, self.right, self.left).hit(self.ball_x_pos, self.ball_y_pos, self.ball_x_speed)
            self.ball_x_pos = result[0]
            self.ball_x_speed = result[1]
            pygame.display.update()

