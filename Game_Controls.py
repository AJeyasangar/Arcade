import pygame
import Pause_Menu
import pygame.math as Mathematics
import Menu
import Wall_Bounce
import Platform_Scores
import Paddles
import time
import random
import Snake_Process


class Game:
    def __init__(self, info):
        pygame.init()
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
        self.speed_increase = 1
        self.speed_val = 7
        self.last_ball_pos = 600

        self.Start_Modes = ["Pong", "Snake", "Quit"]
        self.Start_Menu = self.Start_Modes[0]
        self.Start_Game = "menu"
        self.selected = False
        self.i = 0

        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        self.snake_score = 0
        self.food_pos = [random.randrange(1, (self.width // 10)) * 10, random.randrange(1, (self.height // 10)) * 10]
        self.food_spawn = True
        self.snake_vel = [0, 0]
    @property
    def event_process(self):
        while not self.crashed:
            for event in pygame.event.get():
                if self.Start_Game == 'menu':
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.i > 0:
                            self.i -= 1
                            self.Start_Menu = self.Start_Modes[self.i]
                        elif event.key == pygame.K_DOWN and self.i<2:
                            self.i += 1
                            self.Start_Menu = self.Start_Modes[self.i]
                        if event.key == pygame.K_RETURN:
                            if self.Start_Menu == self.Start_Modes[1] or self.Start_Menu == self.Start_Modes[0]:
                                self.selected = True
                            if self.Start_Menu == "quit":
                                pygame.quit()
                                quit()
                    self.Start_Game = Menu.Menu(self).draw(self)

                if self.Start_Game == "pong":
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.val_y = Mathematics.Vector2(0, self.vector_y)
                        elif event.key == pygame.K_DOWN:
                            self.val_y = Mathematics.Vector2(0, -self.vector_y)
                        if event.key == pygame.K_w:
                            self.val_y2 = Mathematics.Vector2(0, self.vector_y)
                        elif event.key == pygame.K_s:
                            self.val_y2 = Mathematics.Vector2(0, -self.vector_y)
                        if event.key == pygame.K_ESCAPE:
                            Pause_Menu.Pause()
                    if event.type == pygame.KEYUP:
                        self.val_y = Mathematics.Vector2(0, 0)
                        self.val_y2 = Mathematics.Vector2(0, 0)
                if self.Start_Game == "snake":
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.snake_vel[0] = 0
                            self.snake_vel[1] = -10
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            self.snake_vel[0] = 0
                            self.snake_vel[1] = 10
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.snake_vel[1] = 0
                            self.snake_vel[0] = -10
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.snake_vel[1] = 0
                            self.snake_vel[0] = 10

            if self.Start_Game == "pong":
                self.right += self.val_y
                self.left += self.val_y2
                self.screen.fill((0, 0, 0))
                Platform_Scores.Screen(self).score_board()
                result = Paddles.Paddles(self).hit()

                self.ball_pos, self.ball_speed, self.speed_direction, self.speed_val = result
                self.ball_pos = self.ball_pos + self.ball_speed
                result = Wall_Bounce.BounceBoundaries(self).check(self)
                self.ball_pos = result[0]

                self.ball_speed = result[1]
                self.score_left = result[2]
                self.score_right = result[3]
                self.speed_direction = result[4]
                self.speed_val = result[5]
                self.last_ball_pos = result[6]
                self.ball_pos += self.ball_speed
                pygame.draw.circle(self.screen, (255, 255, 255), (int(self.ball_pos[0]), int(self.ball_pos[1])), 7)
                pygame.font.init()
                tfont = pygame.font.Font(None, 28)
                right_text = tfont.render("Right Player Wins", True, (255, 255, 255))
                left_text = tfont.render("Left Player Wins", True, (255, 255, 255))
                textpos = right_text.get_rect(centerx=self.screen.get_width() / 2)
                textpos = left_text.get_rect(centerx=self.screen.get_width() / 2)
                textpos.top = 60
                if self.score_right == 11:
                    self.screen.blit(right_text, textpos)
                    pygame.display.update()
                    pygame.display.flip()
                    time.sleep(8)
                    pygame.quit()

                elif self.score_left == 11:
                    self.screen.blit(left_text, textpos)
                    pygame.display.update()
                    pygame.display.flip()
                    time.sleep(8)
                    pygame.quit()
                self.clock.tick(30)

            if self.Start_Game == "snake":
                self.snake_pos[1] += self.snake_vel[1]
                self.snake_pos[0] += self.snake_vel[0]
                result = Snake_Process.Snake(self).Snake_main(self)
                self.snake_pos = result[0]
                self.snake_body = result[1]
                self.snake_score = result[2]
                self.food_pos = result[3]
                self.food_spawn = result[4]
                self.clock.tick(10)
            pygame.display.flip()
