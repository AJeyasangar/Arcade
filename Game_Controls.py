import pygame
import pygame.math as Mathematics
import Menu
import Wall_Bounce
import Platform_Scores
import Paddles
import random
import Snake_Process
import Breakout_Process
import HighScore


class Game:
    def __init__(self, info):
        self.clock = pygame.time.Clock()
        self.screen = info.screen
        self.val_y = Mathematics.Vector2(0, 0)
        self.val_y2 = Mathematics.Vector2(0, 0)
        self.width = info.width
        self.height = info.height
        self.crashed = False
        self.vector_y = -7
        self.left = Mathematics.Vector2(0, 100)
        self.right = Mathematics.Vector2(self.width - 10, 100)
        self.ball_pos = Mathematics.Vector2(320, 240)
        self.score_left = 0
        self.score_right = 0
        self.ball_speed = Mathematics.Vector2(5)
        self.speed_direction = True
        self.speed_increase = 0.1
        self.speed_val = 7
        self.last_ball_pos = 600
        self.last_bounce = [0, 0]
        self.bg = pygame.image.load("Arcade.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.Start_Modes = ["Pong", "Snake", "Breakout", "quit"]
        self.Start_Menu = self.Start_Modes[0]
        self.Start_Game = "menu"
        self.selected = False
        self.i = 0

        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        self.snake_score = 0
        self.food_pos = [random.randrange(1, (self.width // 10)) * 10, random.randrange(60, (self.height // 10)) * 10]
        self.food_spawn = True
        self.snake_vel = [0, 0]
        self.direction = "RIGHT"
        self.change_to = self.direction

        self.xspeed_init = 6
        self.yspeed_init = 6
        self.max_lives = 5

        self.val_x = 0
        self.bat_speed = 20
        self.score = 0
        self.bat = pygame.image.load("bat.png").convert()
        self.batrect = self.bat.get_rect()

        self.ball = pygame.image.load("ball.png").convert()
        self.ball.set_colorkey((255, 255, 255))
        self.ballrect = self.ball.get_rect()
        self.batrect = self.batrect.move((self.width / 2) - (self.batrect.right / 2), self.height - 20)
        self.ballrect = self.ballrect.move(self.width / 2, self.height / 2)
        self.bat_x = self.batrect[0]
        self.xspeed = self.xspeed_init
        self.yspeed = self.yspeed_init
        self.lives = self.max_lives
        self.first_time = True
        self.wall = Breakout_Process.Wall()
        self.wall.build_wall(self.width)
        self.once = True
        self.max_score = 0
    @property
    def event_process(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.val_y = Mathematics.Vector2(0, self.vector_y)

                    elif event.key == pygame.K_DOWN:
                        self.val_y = Mathematics.Vector2(0, -self.vector_y)

                    elif event.key == pygame.K_RETURN:
                        if self.Start_Menu == self.Start_Modes[1] or self.Start_Menu == self.Start_Modes[0] or self.Start_Menu == self.Start_Modes[2]:
                            self.selected = True
                        if self.Start_Menu == "quit":
                            pygame.quit()
                            quit()
                    elif event.key == pygame.K_w:
                        self.val_y2 = Mathematics.Vector2(0, self.vector_y)
                        self.change_to = "UP"
                    elif event.key == pygame.K_s:
                        self.val_y2 = Mathematics.Vector2(0, -self.vector_y)
                        self.change_to = "DOWN"
                    elif event.key == pygame.K_a:
                        self.change_to = "LEFT"
                    elif event.key == pygame.K_d:
                        self.change_to = "RIGHT"
                    elif event.key == pygame.K_LEFT:
                        self.batrect = self.batrect.move(-self.bat_speed, 0)
                        self.val_x = -self.bat_speed
                    if event.key == pygame.K_RIGHT:
                        self.batrect = self.batrect.move(self.bat_speed, 0)
                        self.val_x = self.bat_speed

                    if event.key == pygame.K_ESCAPE:

                        Game(self).event_process

                if event.type == pygame.KEYUP:
                    self.val_y = Mathematics.Vector2(0, 0)
                    self.val_y2 = Mathematics.Vector2(0, 0)
                    self.val_x = 0

            if self.Start_Game == "menu":
                self.Start_Game = Menu.Menu(self).draw(self)
                self.selected = False
            if self.Start_Game == "pong":
                Game.Pong(self)

            if self.Start_Game == "snake":
                Game.Snake(self)
            if self.Start_Game == "breakout":
                pygame.font.init()
                self.max_score = HighScore.Score("breakout").high_score()

                self.bat_x += self.val_x
                if self.bat_x < 0: self.bat_x = 0
                if self.bat_x > self.width - 80: self.bat_x = self.width - 80
                result = Breakout_Process.Breakout(self).main(self)
                self.xspeed_init, self.yspeed_init, self.max_lives, self.bat_speed, self.score, self.batrect, self.ballrect, self.xspeed, self.yspeed, self.lives = result
                if self.lives <= 0:
                    self.screen.blit(self.bg, (0, 0))
                    msg = pygame.font.Font("arcade.ttf", 70).render("Game Over", True, (255, 255, 255))
                    self.screen.blit(msg, (self.width / 2 - 300, self.height / 2))
                    if self.once:
                        HighScore.Score("breakout").save_score(self.score)
                        self.once = False
                    pygame.display.flip()
            pygame.display.flip()

    def Pong(self):
        self.right += self.val_y
        self.left += self.val_y2
        if int(self.right[1]) <= 0:
            self.right[1] = 0
        if int(self.left[1]) < 0:
            self.left[1] = 0
        if int(self.right[1] + 100) > self.height:
            self.right[1] = self.height - 100
        if int(self.left[1] + 100) > self.height:
            self.left[1] = self.height - 100

        self.screen.blit(self.bg, (0, 0))
        Platform_Scores.Screen(self).score_board()
        result = Paddles.Paddles(self).hit(self)
        self.ball_pos, self.ball_speed, self.speed_direction, self.speed_val, self.last_bounce = result
        self.ball_pos = self.ball_pos + self.ball_speed
        result = Wall_Bounce.BounceBoundaries(self).check(self)

        self.ball_pos, self.ball_speed, self.score_left, self.score_right, self.speed_direction, \
        self.speed_val, self.last_ball_pos, self.last_bounce = result
        self.ball_pos += self.ball_speed
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.ball_pos[0]), int(self.ball_pos[1])), 7)
        pygame.font.init()
        tfont = pygame.font.Font("arcade.ttf", 74)
        right_text = tfont.render("Right Player Wins", True, (255, 255, 255))
        left_text = tfont.render("Left Player Wins", True, (255, 255, 255))
        Game_over = tfont.render("GAME OVER", True, (255, 255, 255))
        textpos = right_text.get_rect(centerx=self.screen.get_width() / 2)
        textpos = left_text.get_rect(centerx=self.screen.get_width() / 2)
        textpos.top = 60
        if self.score_right >= 11:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(right_text, textpos)
            self.screen.blit(Game_over, (self.width/2, self.height/2))
            pygame.display.update()

        elif self.score_left >= 11:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(left_text, textpos)
            self.screen.blit(Game_over, (self.width/2 - 300, self.height/2))
            pygame.display.update()

        self.clock.tick(30)

    def Snake(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10
        self.max_score = HighScore.Score("snake").high_score()
        result = Snake_Process.Snake(self).Snake_main(self)
        self.snake_pos, self.snake_body, self.snake_score, self.food_pos, self.food_spawn = result
        self.clock.tick(10)



