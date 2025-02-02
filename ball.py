from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction_default = 0.3
        self.y_direction_default = 0.3
        # self.movespeed = 0.0000001

    def move(self):
        x = self.xcor() + self.x_direction_default
        y = self.ycor() + self.y_direction_default
        self.goto(x,y)

    def bounce_y(self):
        self.y_direction_default *= -1

    def bounce_x(self):
        self.x_direction_default *= -1
        # self.movespeed *= 0.00000001

    def resetposition(self):
        self.goto(0,0)
        # self.movespeed = 0.0000001
        self.bounce_x()
