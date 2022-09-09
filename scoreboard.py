from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0, 265)
        high_score_file = open("high_score.txt")
        self.high_score = int(high_score_file.read())
        high_score_file.close()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.writer()

    def writer(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Helvetica", 15, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Helvetica", 15, "normal"))
