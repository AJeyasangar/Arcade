import pygame
import time

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = "Airstream.ttf"

    def draw(self, Start_Menu, Start_Game, selected, Start_Modes):
        title = "The Arcade"
        text_Pong= "Pong"
        text_Snake = "Snake"
        text_quit = "Quit"
        print(Start_Menu)
        self.screen.fill((0, 0, 255))
        title = text_format(title, self.font, 90, (255, 255, 255))

        if Start_Menu == Start_Modes[0]:
            text_Pong= text_format(text_Pong, self.font, 75, (255, 255, 255))
            if selected:
                Start_Game = "pong"
        else:
            text_Pong = text_format(text_Pong, self.font, 75, (0, 0, 0))
        if Start_Menu == Start_Modes[1]:
            text_Snake = text_format(text_Snake, self.font, 75, (255, 255, 255))
            if selected:
                Start_Game = "snake"
        else:
            text_Snake = text_format(text_Snake, self.font, 75, (0, 0, 0))

        if Start_Menu == Start_Modes[2]:
            text_quit = text_format(text_quit, self.font, 75, (255, 255, 255))
            if selected:
                pygame.quit()
        else:
            text_quit = text_format(text_quit, self.font, 75, (0, 0, 0))

        title_rect = title.get_rect()
        Pong_rect = text_Pong.get_rect()
        Snake_rect = text_Snake.get_rect()
        quit_rect = text_quit.get_rect()

        self.screen.blit(title, (self.width/2 - (title_rect[2]/2), 80))
        self.screen.blit(text_Pong, (self.width/2 - (Pong_rect[2]/2), 300))
        self.screen.blit(text_Snake, (self.width / 2 - (Snake_rect[2] / 2), 360))
        self.screen.blit(text_quit, (self.width/2 - (quit_rect[2]/2), 420))
        return Start_Game


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

