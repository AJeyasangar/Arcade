import pygame, Ball, Paddles


class Game:
    def __init__(self):
        pygame.init()
        global screen
        screen = pygame.display.set_mode((1200, 600))
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.left = [0, 100]
        self.right = [1190, 0]
        self.val_y = [0, 0]
        self.clock = pygame.time.Clock()

    def event_process(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.val_y[0] = -5
                    if event.key == pygame.K_DOWN:
                        self.val_y[0] = 5
                    if event.key == pygame.K_w:
                        self.val_y[1] = -5
                    if event.key == pygame.K_s:
                        self.val_y[1] = 5

                if event.type == pygame.KEYUP:
                    self.val_y[0] = 0; self.val_y[1] = 0
            self.right[1] += self.val_y[0]
            self.left[1] += self.val_y[1]
            screen.fill((0, 0, 0))
            Paddles.Paddles(screen, self.left)
            Paddles.Paddles(screen, self.right)
            Ball.Ball(screen)
            self.clock.tick(30)
            pygame.display.update()
            pygame.display.update()
        pygame.quit()
        quit()






Game().event_process()
