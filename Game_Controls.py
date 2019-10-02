import pygame
import Ball
import Paddles


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.left = [0, 100]
        self.right = [1190, 0]
        self.val_y = [0, 0]
        self.clock = pygame.time.Clock()
        self.bal_pos = [0, 0]
        self.speed = 1

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
            self.bal_pos[0] += 1
            self.bal_pos[1] += 1
            self.screen.fill((0, 0, 0))
            Paddles.Paddles(self.screen, self.right)
            Paddles.Paddles(self.screen, self.left)
            Ball.Ball(self.screen, self.bal_pos).draw()
            pygame.display.update()
