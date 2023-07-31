from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('./highscore.txt', mode='r') as highscore:
            self.high_score = highscore.read()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 250)
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align='center', font=('Calibri', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align='center', font=('Calibri', 20, 'bold'))

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open('./highscore.txt', mode='w') as highscore:
                highscore.write(self.high_score)
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align='center', font=('Calibri', 20, 'bold'))


