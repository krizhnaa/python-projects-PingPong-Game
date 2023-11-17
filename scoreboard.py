from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_card()
        self.r_card()

    def r_card(self):
        self.goto(100, 175)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_card(self):
        self.goto(-100, 175)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))

    def r_scored(self):
        self.r_score += 1
        self.clear()
        self.r_card()

    def l_scored(self):
        self.l_score += 1
        self.clear()
        self.l_card()

