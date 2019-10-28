import pygame
import pygame.math as Mathematics


class Control:


    def controller(info):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if info.i > 0:
                        info.i -= 1
                        info.Start_Menu = info.Start_Modes[info.i]
                    info.val_y = Mathematics.Vector2(0, info.vector_y)
                    info.snake_vel[0] = 0
                    info.snake_vel[1] = -10
                elif event.key == pygame.K_DOWN:
                    if info.i < 2:
                        info.i += 1
                        info.Start_Menu = info.Start_Modes[info.i]

                    info.val_y = Mathematics.Vector2(0, -info.vector_y)
                    info.snake_vel[0] = 0
                    info.snake_vel[1] = 10
                elif event.key == pygame.K_RETURN:
                    if info.Start_Menu == info.Start_Modes[1] or info.Start_Menu == info.Start_Modes[0]:
                        info.selected = True
                    if info.Start_Menu == "quit":
                        pygame.quit()
                        quit()
                elif event.key == pygame.K_w:
                    info.val_y2 = Mathematics.Vector2(0, info.vector_y)
                elif event.key == pygame.K_s:
                    info.val_y2 = Mathematics.Vector2(0, -info.vector_y)
                elif event.key == pygame.K_LEFT:
                    info.snake_vel[1] = 0
                    info.snake_vel[0] = -10
                elif event.key == pygame.K_RIGHT:
                    info.snake_vel[1] = 0
                    info.snake_vel[0] = 10
            if event.type == pygame.KEYUP:
                info.val_y = Mathematics.Vector2(0, 0)
                info.val_y2 = Mathematics.Vector2(0, 0)
            return info.i, info.Start_Menu, info.Start_Modes, info.val_y, info.vector_y, info.snake_vel, info.selected, info.val_y2, info.snake_vel
