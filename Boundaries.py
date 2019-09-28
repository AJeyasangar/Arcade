#This program is used to make sure that the paddles dont got out of the screen. It is also used to check if the ball touches the wall on the left or right which means that the player has lost the game. If the ball touches the top or bottom part of the screem it should make the ball to bounce.



class Walls:
    def init(self, dimensions, ball_pos):
        self.dimensions = dimensions
        self.ball_pos = ball pos