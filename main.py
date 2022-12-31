from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('pong')
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle2.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1) < 45 and ball.xcor() > 360 or ball.distance(paddle2) < 45 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.restart_position()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.restart_position()
        scoreboard.l_point()

screen.exitonclick()
