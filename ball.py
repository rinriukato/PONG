from turtle import Turtle
from time import sleep

DEFAULT_SPEED = 5
SPEED_INCREASE = 0.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_dir = 1
        self.y_dir = 1
        self.speed = DEFAULT_SPEED
        self.last_hit_paddle = None

    def move(self):
        new_x = self.xcor() + (self.speed * self.x_dir)
        new_y = self.ycor() + (self.speed * self.y_dir)
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_dir *= -1

    def bounce_paddle(self):
        self.x_dir *= -1

    def increase_speed(self):
        self.speed += SPEED_INCREASE

    def reset_ball(self):
        self.goto(0, 0)
        self.speed = DEFAULT_SPEED
        self.last_hit_paddle = None
        sleep(0.5)

    def set_paddle_last_hit(self, paddle):
        self.last_hit_paddle = paddle
