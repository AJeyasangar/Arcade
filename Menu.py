import pygame
import Game_Controls
import Buttons


class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 34)

    def draw(self):
        print("here")
        text = "Welcome to Pong"
        Menu_text = self.font.render(text, True, (255, 255, 255))
        text_pos = Menu_text.get_rect(centerx=self.width / 2)
        self.screen.blit(Menu_text, text_pos)
        self.button_01 = Buttons.Button("Game", self.screen, (85, 190))
        self.buttons = [self.button_01]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.rect.collidepoint(pos):
                            Buttons.button.call_back()

            for button in self.buttons:
                Buttons.Button("Game", self.screen, (85, 190)).draw

            pygame.display.flip()
            pygame.time.wait(40)


