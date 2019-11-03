import pygame
import random

class Breakout:
    def __init__(self, info):
        self.screen = info.screen
        self.width = info.width
        self.height = info.height
        self.bat =info.bat
        self.batrect = info.batrect
        self.bgcolour = (0, 0, 0)
        self.bg = pygame.image.load("Arcade.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.ball = info.ball
        self.ball.set_colorkey((255, 255, 255))
        self.ballrect = info.ballrect

        self.Bounce = pygame.mixer.Sound('Blip_1-Surround-147.wav')
        self.Bounce.set_volume(10)
        self.max_score = info.max_score


    def main(self, info):

        if info.ballrect.bottom >= info.batrect.top and info.ballrect.bottom <= info.batrect.bottom and info.ballrect.right >= info.batrect.left and info.ballrect.left <= info.batrect.right:
            info.yspeed = -info.yspeed
            self.Bounce.play(0)
            offset = info.ballrect.center[0] - info.batrect.center[0]
            if offset > 0:
                if offset > 30:
                    info.xspeed = 7
                elif offset > 23:
                    info.xspeed = 6
                elif offset > 17:
                    info.xspeed = 5
            else:
                if offset < -30:
                    info.xspeed = -7
                elif offset < -23:
                    info.xspeed = -6
                elif info.xspeed < -17:
                    info.xspeed = -5

        info.ballrect = info.ballrect.move(info.xspeed, info.yspeed)
        if info.ballrect.left < 0 or info.ballrect.right > self.width:
            info.xspeed = -info.xspeed
            self.Bounce.play(0)
        if info.ballrect.top < 0:
            info.yspeed = -info.yspeed
            self.Bounce.play(0)
        if info.ballrect.top > self.height:
            info.lives -= 1
            info.xspeed = info.xspeed_init
            rand = random.random()
            if random.random() > 0.5:
                info.xspeed = -info.xspeed
            info.yspeed = info.yspeed_init
            info.ballrect.center = self.width * random.random(), self.height / 3

        if info.xspeed < 0 and info.ballrect.left < 0:
            info.xspeed = -info.xspeed
            self.Bounce.play(0)

        if info.xspeed > 0 and info.ballrect.right > self.width:
            info.xspeed = -info.xspeed
            self.Bounce.play(0)

        index = info.ballrect.collidelist(info.wall.brickrect)
        if index != -1:
            if info.ballrect.center[0] > info.wall.brickrect[index].right or \
                    info.ballrect.center[0] < info.wall.brickrect[index].left:
                info.xspeed = -info.xspeed
            else:
                info.yspeed = -info.yspeed
            self.Bounce.play(0)
            info.wall.brickrect[index:index + 1] = []
            info.score += 10

        self.screen.blit(self.bg, (0, 0))
        high_score_msg = pygame.font.Font("arcade.ttf", 20).render("Highest Score:" + str(self.max_score), True,
                                                                   (255, 255, 255))
        self.screen.blit(high_score_msg, (30, 20))
        scoretext = pygame.font.Font("arcade.ttf", 20).render("Score:" + str(info.score), True, (255, 255, 255))
        self.screen.blit(scoretext, (self.width - 200, 20))

        for i in range(0, len(info.wall.brickrect)):
            self.screen.blit(info.wall.brick, info.wall.brickrect[i])

        if info.wall.brickrect == []:
            info.wall.build_wall(self.width)
            info.xspeed = info.xspeed_init
            info.yspeed = info.yspeed_init
            info.ballrect.center = self.width / 2, self.height / 3
        info.batrect[0] = info.bat_x
        self.screen.blit(self.ball, info.ballrect)
        self.screen.blit(self.bat, (info.bat_x, self.height - 20))
        return info.xspeed_init, info.yspeed_init, info.max_lives, info.bat_speed, info.score, info.batrect, info.ballrect, info.xspeed, info.yspeed, info.lives


class Wall():
    def __init__(self):
        self.brick = pygame.image.load("brick.png").convert()
        brickrect = self.brick.get_rect()
        self.bricklength = brickrect.right - brickrect.left
        self.brickheight = brickrect.bottom - brickrect.top

    def build_wall(self, width):
        xpos = 0
        ypos = 60
        adj = 0
        self.brickrect = []
        for i in range (0, 52):
            if xpos > width:
                if adj == 0:
                    adj = self.bricklength / 2
                else:
                    adj = 0
                xpos = -adj
                ypos += self.brickheight

            self.brickrect.append(self.brick.get_rect())
            self.brickrect[i] = self.brickrect[i].move(xpos, ypos)
            xpos = xpos + self.bricklength
