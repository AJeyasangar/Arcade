import pygame
import random
import Game_Controls
import time


class Snake:
    def __init__(self, info):
        self.screen = info.screen
        self.width = info.width
        self.height = info.height
        self.font = "Airstream.ttf"
        pygame.init()

    def Snake_main(self, info):

        global display
        display = self.screen
        info.snake_body.insert(0, list(info.snake_pos))
        if info.snake_pos[0] == info.food_pos[0] and info.snake_pos[1] == info.food_pos[1]:
            info.snake_score += 1
            info.food_spawn = False
        else:
            info.snake_body.pop()
        if not info.food_spawn:
            info.food_pos = [random.randrange(1, (self.width // 10)) * 10, random.randrange(1, (self.height // 10)) * 10]
        info.food_spawn = True
        self.screen.fill((0, 0, 0))
        for pos in info.snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(info.food_pos[0], info.food_pos[1], 10, 10))
        if info.snake_pos[0] < 0 or info.snake_pos[0] > self.width - 10:
            game_over(self.width, self.height)
        if info.snake_pos[1] < 0 or info.snake_pos[1] > self.height:
            game_over(self.width, self.height)
        """for block in info.snake_body[1:]:
            if info.snake_pos[0] == block[0] and info.snake_pos[1] == block[1]:
                game_over(self.width, self.height)"""
        Snake.show_score(self, 1, (255, 255, 255), self.font, 20, info.snake_score)
        return info.snake_pos, info.snake_body, info.snake_score, info.food_pos, info.food_spawn

    def show_score(self, choice, color, font, size, snake_score):
        pygame.font.init()
        print("here")
        score_font = pygame.font.Font(font, size)
        score_surface = score_font.render('Score : ' + str(snake_score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.width / 10, 15)
        else:
            score_rect.midtop = (self.width / 2, self.height / 1.25)
        return score_surface, score_rect
        display.blit(score_surface, score_rect)


def game_over(width, height):
    my_font = pygame.font.Font('Airstream.ttf', 90)
    game_over_surface = my_font.render('YOU DIED', True, (0, 0, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    display.fill((0, 0, 0))
    display.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
