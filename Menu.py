import pygame


class Menu:
    def __init__(self, info):
        self.screen = info.screen
        self.width = info.width
        self.height = info.height
        self.font = "arcade.ttf"
        self.bg = pygame.image.load("Arcade.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.pong_image = pygame.image.load('Pong.jpg')
        self.pong_image = pygame.transform.scale(self.pong_image, (self.width//3, self.height//3))
        self.snake_image = pygame.image.load('snake.png')
        self.snake_image = pygame.transform.scale(self.snake_image, (self.width // 3, self.height // 3))
        self.breakout_image = pygame.image.load('Breakout.png')
        self.breakout_image = pygame.transform.scale(self.breakout_image, (self.width // 3, self.height // 3))
        self.pong_image_rect = self.pong_image.get_rect()
        self.mouse = pygame.mouse.get_pos()

    def draw(self, info):
        title = "The Arcade"
        text_Pong= "Pong"
        text_Snake = "Snake"
        text_Breakout = "Breakout"
        text_quit = "Quit"
        game = "Game:"
        game = text_format(game, self.font, 40, (255, 255, 255))
        text_quit = text_format(text_quit, self.font, 35, (255, 255, 255))
        title = text_format(title, self.font, 90, (255, 255, 255))
        title_rect = title.get_rect()
        quit_rect = text_quit.get_rect()
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(title, (self.width / 2 - (title_rect[2] / 2), 40))
        self.screen.blit(text_quit, (10, self.height - 50))
        self.screen.blit(self.pong_image, (self.width//13, (self.height*2) // 10))
        self.screen.blit(self.snake_image, (self.width-600, (self.height*2) // 10))
        self.screen.blit(self.breakout_image, (350, (self.height*6) // 10))
        size_x, size_y = self.width // 3, self.height // 3
        pong_x, pong_y = self.width//13, self.height*2 // 10
        snake_x, snake_y = self.width// 2.25, self.height*2//10
        breakout_x, breakout_y = self.width//3.5, self.height*6 // 10
        quit_x, quit_y = 10, self.height - 50

        if pong_x + size_x >= self.mouse[0] >= pong_x and (pong_y + size_y) >= self.mouse[1] >= pong_y-10:
            text_Pong= text_format(text_Pong, self.font, 35, (233, 44, 22))
            pygame.draw.rect(self.screen, (233, 44, 22), (95, (self.height*2)//10 -5, self.width//3+10, self.height//3+10))
            self.screen.blit(self.pong_image, (100, (self.height * 2) // 10))
            self.screen.blit(text_Pong, (self.width- 200, self.height-50))
            self.screen.blit(game, (self.width - 400, self.height - 50))
            if info.selected:
                info.Start_Game = "pong"

        if snake_x+size_x >= self.mouse[0] >= snake_x and snake_y + size_y >= self.mouse[1] >= snake_y:
            text_Snake = text_format(text_Snake, self.font, 35, (233, 44, 22))
            pygame.draw.rect(self.screen, (233, 44, 22),(self.width-605, (self.height * 2) // 10 - 5, self.width // 3 + 10, self.height // 3 + 10))
            self.screen.blit(self.snake_image, (self.width-600, (self.height * 2) // 10))
            self.screen.blit(text_Snake, (self.width- 200, self.height-50))
            self.screen.blit(game, (self.width - 400, self.height - 50))
            if info.selected:
                info.Start_Game = "snake"

        if breakout_x + size_x >= self.mouse[0] >= breakout_x and breakout_y + breakout_y >= self.mouse[1] >= breakout_y:
            text_Breakout = text_format(text_Breakout, self.font, 35, (233, 44, 22))
            pygame.draw.rect(self.screen, (233, 44, 22), (350, (self.height * 6) //10 - 5, self.width // 3 + 10, self.height // 3 + 10))
            self.screen.blit(self.breakout_image, (355, (self.height * 6) // 10))
            self.screen.blit(text_Breakout, (self.width- 300, self.height-50))
            self.screen.blit(game, (self.width - 500, self.height - 50))
            if info.selected:
                info.Start_Game = "breakout"

        if quit_x + quit_rect[2] > self.mouse[0] > quit_x and quit_y + quit_rect[3] > self.mouse[1] > quit_y- 110:
            text_quit = "Quit"
            text_quit = text_format(text_quit, self.font, 35, (233, 44, 22))
            self.screen.blit(text_quit, (10, self.height - 50))
            if info.selected:
                pygame.quit()
        return info.Start_Game


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

