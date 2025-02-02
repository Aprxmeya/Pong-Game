from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import time, sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1500, height=800)
screen.title("Classic Pong")
screen.tracer(0)

l = Paddle((-700,0))
r = Paddle((700,0))
b = Ball()
s = Scoreboard()

screen.listen()

screen.onkey(r.go_up,"Up")
screen.onkey(r.go_down,"Down")
screen.onkey(l.go_up,"w")
screen.onkey(l.go_down,"s")

game = True
while game:
    # sleep(b.movespeed)
    screen.update()
    b.move()

    if b.ycor() > 380 or b.ycor() < -380:
        b.bounce_y()

    if b.xcor() > 340 and b.distance(r) < 30 or b.xcor() < -340 and b.distance(l) < 30:
         b.bounce_x()

    if b.xcor() > 750:
        b.resetposition()
        s.scoreleft()

    if b.xcor() < -750:
        b.resetposition()
        s.scoreright()





screen.exitonclick()