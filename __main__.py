#This links all the programs together so the program can work
import Game_Controls
import Ball
import Paddles
import Boundaries


class Game:
    def __init__(self):
        self.Controls = Game_Controls()
        self.Ball = Ball()
        self.Paddles = Paddles()
        self.Boundaries = Boundaries()

    def Run(self):
        pass




