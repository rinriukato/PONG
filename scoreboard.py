from turtle import Turtle

FONT = "Arial"
FONT_SIZE = 15
FONT_TYPE = 'normal'
START_X_COORD = 0
START_Y_COORD = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color('white')
        self.hideturtle()
        self.goto(START_X_COORD, START_Y_COORD)
        self.update_text()

    def increment_score_p1(self):
        self.p1_score += 1
        self.update_text()

    def increment_score_p2(self):
        self.p2_score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(arg=f"{self.p1_score} | {self.p2_score}", move=False, align='center',
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def end_game_text(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align='center',
                   font=(FONT, FONT_SIZE, FONT_TYPE))
