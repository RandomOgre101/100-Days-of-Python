from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(0,260)
        self.hideturtle()
        self.write_score()
        

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.write_score() 

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER.", False, align=ALIGN, font=('Arial', 18, 'normal'))


    def increase_score(self):
        self.score += 1
        self.write_score()
