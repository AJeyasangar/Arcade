import math as Mathematics


class Angle:
    def __init__(self, ball_pos, ball_speed, speed_direction, last_bounce, width):
        self.ball_pos = ball_pos
        self.ball_speed = ball_speed
        self.speed_direction = speed_direction
        self.last_bounce = last_bounce
        self.width = width

    @property
    def calculate(self):
        x_difference = self.width - 12 - self.last_bounce[1]
        loop = x_difference // self.ball_speed[0]
        if self.ball_pos[1] < 350:
            paddle_y_pos = self.last_bounce[1] + (loop * self.ball_speed[0])
        else:
            paddle_y_pos = self.last_bounce[1] - (loop * self.ball_speed[0])
        
        paddle_y_pos -= 50
        hypotenuse = (((self.last_bounce[1] - paddle_y_pos)**2) + ((self.last_bounce[0] - 1188)**2))**0.5
        horizontal = abs(self.last_bounce[0] - 1188)
        incidence_angle = Mathematics.acos(horizontal / hypotenuse)
        
        incidence_angle = Mathematics.degrees(incidence_angle)
        
        return incidence_angle
