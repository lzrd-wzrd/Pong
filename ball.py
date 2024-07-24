from turtle import Turtle
import random
import time
START_POSITION = (0, 0)
y_choice = [-1, 1]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('magenta')
        self.penup()
        self.goto(START_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.05:
            self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= random.choice(y_choice)
        self.move()
