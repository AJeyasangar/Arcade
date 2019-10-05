import pygame
import Paddles
import BounceBall


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.left = [0, 100]
        self.right = [630, 0]
        self.val_y = [0, 0]
        self.clock = pygame.time.Clock()
        self.speed = 5
        self.pos_x = int(0.5 * 640)
        self.pos_y = int(0.5 * 480)
        self.score_left = 0
        self.score_right = 0
        self.speed_x = 3
        self.speed_y = 3

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
            pygame.draw.rect(self.screen, (255, 255, 255), (self.right[0], self.right[1], 10, 100))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.left[0], self.left[1], 10, 100))
            #self.speed_x = Paddles.Paddles(self.screen, self.right, self.left, self.pos_x, self.pos_y, self.speed_x).hit()
            self.pos_x = self.pos_x + 3
            if self.pos_x > 640:
                if self.pos_y > (0.5 * 480):
                    self.speed_y = abs(self.speed_y)
                else:
                    self.speed_y = -abs(self.speed_y)
                self.pos_x = int(0.5 * 640)
                self.pos_y = int(0.5 * 480)
                self.score_left += 1
            elif self.pos_x < 0:
                if self.pos_y > (0.5 * 480):
                    self.speed_y = abs(3)
                else:
                    self.speed_y = -abs(3)
                self.pos_x = int(0.5 * 640)
                self.pos_y = int(0.5 * 480)
                self.score_right += 1
            self.pos_y = self.pos_y + self.speed_y
            if self.pos_y > 480:
                self.speed_y = -3
            elif self.pos_y < 0:
                self.speed_y = abs(3)
            pygame.draw.circle(self.screen, (255, 255, 255), [self.pos_x, self.pos_y], 4)
            if self.pos_x <= (22) and self.pos_y >= int(0.5 * 480 - 0.5 * 100) and self.pos_y <= (int(0.5 * 480 - 0.5 * 100) + 10):
                self.pos_x = 22
                self.speed_x = abs(self.speed_x)
            elif self.pos_x >= 618 and self.pos_y >= int(0.5 * 480 - 0.5 * 100) and self.pos_y <= (int(0.5 * 480 - 0.5 * 100) + 100):
                self.pos_x = 618
                self.speed_x = -self.speed_x

            pygame.display.update()

