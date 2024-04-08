from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

PLAYER_1_START_POS = -380
PLAYER_2_START_POS = 380
GAME_SPEED = 0.02
Y_BOUNDS = 300
X_BOUNDS = 380
PADDLE_COLLISION_DIST = 20
POINTS_TO_WIN = 10

# Initialize Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initialize Paddles
player_1 = Paddle()
player_2 = Paddle()
player_1.set_position(PLAYER_1_START_POS, 0)
player_2.set_position(PLAYER_2_START_POS, 0)

# Initialize Ball
ball = Ball()

# Initialize Scoreboard
scoreboard = Scoreboard()

# Key-Input Event Listeners
screen.listen()
screen.onkeypress(fun=player_1.move_up, key="w")
screen.onkeypress(fun=player_1.move_down, key="s")
screen.onkeypress(fun=player_2.move_up, key="Up")
screen.onkeypress(fun=player_2.move_down, key="Down")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    sleep(GAME_SPEED)
    ball.move()

    # Check if the ball is at the upper boundaries
    if ball.ycor() > Y_BOUNDS or ball.ycor() < -Y_BOUNDS:
        ball.bounce_wall()

    # Check if the ball for paddle collision
    if ball.last_hit_paddle != player_1 and ball.distance(player_1) < PADDLE_COLLISION_DIST:
        ball.set_paddle_last_hit(player_1)
        ball.bounce_paddle()
        ball.increase_speed()

    if ball.last_hit_paddle != player_2 and ball.distance(player_2) < PADDLE_COLLISION_DIST:
        ball.set_paddle_last_hit(player_2)
        ball.bounce_paddle()
        ball.increase_speed()

    # Check if the ball for side boundaries. If > X_bound, then Player 1 Scores, else player 2
    if ball.xcor() > X_BOUNDS:
        scoreboard.increment_score_p1()
        ball.reset_ball()

    if ball.xcor() < -X_BOUNDS:
        scoreboard.increment_score_p2()
        ball.reset_ball()

    if scoreboard.p1_score >= POINTS_TO_WIN or scoreboard.p2_score >= POINTS_TO_WIN:
        scoreboard.end_game_text()
        game_is_on = False


screen.exitonclick()
