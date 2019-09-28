import pygame


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
                    if event.type == pygame.K_UP:
                        self.val_y[0] = 5
                    if event.type == pygame.K_w:
                        self.val_y[1] = -5
                    if event.type == pygame.K_s:
                        self.val_y[1] = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_w or event.key == pygame.K_s:
                        self.val_y[0] = 0
                        self.val_y[1] = 0
            self.right[1] += self.val_y[0]
            self.left[1] += self.val_y[1]
            screen.fill((0, 0, 0))
            Paddles(self.left)
            Paddles(self.right)
            Ball()
            self.clock.tick(30)
            pygame.display.update()
            pygame.display.update()
        pygame.quit()
        quit()


class Paddles:
    def __init__(self, pos):
        pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], 10, 100))

    def paddle_boundaries(self):
        pass


class Ball:
    def __init__(self):
        pygame.draw.circle(screen, (255, 255, 255), (50, 50), 10)

    def ballangles(self):
        pass


class WallBoundaries:
    def __init__(self):
        pass


game = Game()
game.event_process()
