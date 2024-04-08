from turtle import Turtle

MOVE_SPEED = 20
Y_BOUNDS = 280


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=3)

    def set_position(self, x_cord: int, y_cord: int):
        self.setposition(x_cord, y_cord)

    def move_up(self):
        if self.ycor() <= Y_BOUNDS:
            new_y = self.ycor() + MOVE_SPEED
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() >= -Y_BOUNDS:
            new_y = self.ycor() - MOVE_SPEED
            self.goto(self.xcor(), new_y)
