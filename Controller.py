import pygame


class Control():
    def __init__(self):
        pass
    def controller(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
            if event.type == pygame.KEYUP:
                pass