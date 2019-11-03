import pygame
import random
import HighScore


class Snake:
    def __init__(self, info):
        self.screen = info.screen
        self.width = info.width
        self.height = info.height
        self.font = "arcade.ttf"
        self.bg = pygame.image.load("Arcade.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.snake_score = info.snake_score
        self.max_score = info.max_score
        pygame.init()

    def Snake_main(self, info):


        info.snake_body.insert(0, list(info.snake_pos))
        if info.snake_pos[0] == info.food_pos[0] and info.snake_pos[1] == info.food_pos[1]:
            info.snake_score += 1
            info.food_spawn = False
        else:
            info.snake_body.pop()
        if not info.food_spawn:
            info.food_pos = [random.randrange(1, (self.width // 10)) * 10, random.randrange(1, (self.height // 10)) * 10]
        info.food_spawn = True
        self.screen.blit(self.bg, (0, 0))
        for pos in info.snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(info.food_pos[0], info.food_pos[1], 10, 10))
        if info.snake_pos[0] < 0 or info.snake_pos[0] > self.width - 10:
            Snake.game_over(self, info)
        if info.snake_pos[1] < 0 or info.snake_pos[1] > self.height:
            Snake.game_over(self, info)
        for block in info.snake_body[1:]:
            if info.snake_pos[0] == block[0] and info.snake_pos[1] == block[1] or info.once == False:
                Snake.game_over(self, info)
        Snake.show_score(self, 1, (255, 255, 255), self.font, 20, info.snake_score)
        return info.snake_pos, info.snake_body, info.snake_score, info.food_pos, info.food_spawn

    def show_score(self, choice, color, font, size, snake_score):
        pygame.font.init()
        high_score_msg = pygame.font.Font("arcade.ttf", 20).render("Highest Score:" + str(self.max_score), True,
                                                                   (255, 255, 255))
        self.screen.blit(high_score_msg, (self.width - 400, 20))
        score_font = pygame.font.Font(font, size)
        score_surface = score_font.render('Score : ' + str(snake_score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.width / 10, 15)
        else:
            score_rect.midtop = (self.width / 2, self.height / 1.25)
        self.screen.blit(score_surface, score_rect)
        return score_surface, score_rect

    def game_over(self, info):
        self.screen.blit(self.bg, (0, 0))
        my_font = pygame.font.Font('arcade.ttf', 90)
        you_died = my_font.render('YOU DIED', True, (0, 0, 255))
        game_over = my_font.render('GAME OVER', True, (0, 0, 255))
        you_died_rect, game_over_rect = you_died.get_rect(), game_over.get_rect()
        you_died_rect.midtop = (self.width / 2, self.height / 4)
        game_over_rect.midtop = (self.width / 2, self.height*3/ 4)
        if info.once:
            HighScore.Score("snake").save_score(self.snake_score)
            info.once = False
        self.screen.blit(you_died, you_died_rect)
        self.screen.blit(game_over, game_over_rect)
        pygame.display.flip()
