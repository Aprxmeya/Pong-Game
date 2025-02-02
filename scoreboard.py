from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.lscore = 0
        self.rscore = 0

        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.goto(-120, 275)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(120, 275)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))


    def scoreleft(self):
        self.lscore += 1
        self.updatescoreboard()

    def scoreright(self):
        self.rscore += 1
        self.updatescoreboard()
