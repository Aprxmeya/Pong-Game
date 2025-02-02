from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_coordinate = self.ycor() + 75
        self.goto(self.xcor(), y_coordinate)

    def go_down(self):
        y_coordinate = self.ycor() - 75
        self.goto(self.xcor(), y_coordinate)

