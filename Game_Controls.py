import pygame
import Pause_Menu
import pygame.math as Mathematics
import Menu
import Paddle_Process
import Wall_Bounce
import Platform_Scores
import Paddles
import time


class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.val_y = Mathematics.Vector2(0, 0)
        self.val_y2 = Mathematics.Vector2(0, 0)
        self.width = width
        self.height = height
        self.crashed = False
        self.vector_y = -7
        self.left = Mathematics.Vector2(0, 100)
        self.right = Mathematics.Vector2(1190, 100)
        self.ball_pos = Mathematics.Vector2(320, 240)
        self.score_left = 0
        self.score_right = 0
        self.ball_speed = Mathematics.Vector2(5)
        self.speed_direction = True
        self.speed_increase = 1
        self.speed_val = 5
        self.last_ball_pos = 600

        self.Start_Modes = ["Pong", "Snake", "Quit"]
        self.Start_Menu = self.Start_Modes[0]
        self.Start_Game = "menu"
        self.selected = False
        self.i = 0

    @property
    def event_process(self):
        while not self.crashed:
            for event in pygame.event.get():
                if self.Start_Game == 'menu':
                    print("e")
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.i>0:
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
                    self.Start_Game = Menu.Menu(self.screen, self.width, self.height).draw(self.Start_Menu, self.Start_Game, self.selected, self.Start_Modes)

                elif self.Start_Game == "pong":
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
                elif self.Start_Game == "snake":
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or pygame.K_w:
                            pass
                        elif event.key == pygame.K_DOWN or pygame.K_s:
                            pass
                        elif event.key == pygame.K_LEFT or pygame.K_a:
                            pass
                        elif event.key == pygame.K_RIGHT or pygame.K_d:
                            pass

            if self.Start_Game == "pong":
                self.right += self.val_y
                self.left += self.val_y2
                self.screen.fill((0, 0, 0))
                Platform_Scores.Screen(self.screen, self.width, self.score_left, self.score_right).score_board()
                result = Paddles.Paddles(self.screen, self.right, self.left, self.ball_pos, self.ball_speed,
                                         self.speed_direction, self.speed_val, self.speed_increase, self.last_ball_pos).hit()

                self.ball_pos = result[0]
                self.ball_speed = result[1]
                self.speed_direction = result[2]
                self.speed_val = result[3]
                self.ball_pos = self.ball_pos + self.ball_speed
                result = Wall_Bounce.BounceBoundaries(self.ball_pos, self.ball_speed, self.width, self.height,
                                                      self.speed_val, self.last_ball_pos).check(self.score_left, self.score_right,
                                                                                      self.speed_direction)
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
                if self.score_right == 2:
                    self.screen.blit(right_text, textpos)
                    time.sleep(3)
                    pygame.display.flip()
                    pygame.quit()
                elif self.score_left == 2:
                    self.screen.blit(left_text, textpos)
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.quit()
                pygame.display.update()
            if self.Start_Game == "snake":
                s

            pygame.display.flip()


