from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 5)
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(start_pos)
        self.paddle_distance = 20
        self.speed(0)

    def up(self):
        self.forward(self.paddle_distance)

    def down(self):
        self.backward(self.paddle_distance)
