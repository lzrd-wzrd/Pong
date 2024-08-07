from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

scoreboard.player_1 = screen.textinput('', "Player 1 name?")
scoreboard.player_2 = screen.textinput('', "Player 2 name?")
scoreboard.update_scoreboard()

y_choice = [-1, 1]
game_on = True
while game_on:
    screen.listen()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when right paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        screen.update()
        time.sleep(1)

    #Detect when left paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        screen.update()
        time.sleep(1)

screen.exitonclick()

