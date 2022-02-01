# Pong using Turtle
# Ajay Melekamburath (https://ajay-mk.github.io)

import turtle, random

# Game Window Setup
game = turtle.Screen()
game.title("Pong by Turtle")
game.setup(width=800, height=600)
game.bgcolor("white")
game.tracer(0)

# Opponenet Setup
opponent_paddle = turtle.Turtle()
opponent_paddle.speed(0)
opponent_paddle.penup()
opponent_paddle.color("black")
opponent_paddle.shape("square")
opponent_paddle.shapesize(stretch_wid=5, stretch_len=1)
opponent_paddle.goto(-370, 0)

# Player Setup
player_paddle = turtle.Turtle()
player_paddle.speed(0)
player_paddle.penup()
player_paddle.color("black")
player_paddle.shape("square")
player_paddle.shapesize(stretch_wid=5, stretch_len=1)
player_paddle.goto(370, 0)


# Ball Setup
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.color("black")
ball.shape("circle")
ball.goto(0,0)
# Ball Movement Speed
ball.dx = 0.0275
ball.dy = 0.0275

#Scoring
score_p = 0
score_o = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("black")
score.shape("square")
score.hideturtle()
score.goto(0, -270)
score.write("Player: 0  Opponent: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def p_paddle_up():
    y = player_paddle.ycor()
    y += 25
    player_paddle.sety(y)

def p_paddle_down():
    y = player_paddle.ycor()
    y -= 25
    player_paddle.sety(y)

def o_paddle_up():
    y = opponent_paddle.ycor()
    y += 25
    opponent_paddle.sety(y)

def o_paddle_down():
    y = opponent_paddle.ycor()
    y -= 25
    opponent_paddle.sety(y)
    
# Keyboard Bindings
game.listen()
game.onkey(p_paddle_up, "Up")
game.onkey(p_paddle_down, "Down")
game.onkey(o_paddle_up, "w")
game.onkey(o_paddle_down, "s")

# Main Game Loop
while True:
    game.update()
    
    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Bouncing on top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # Left and Right Boundaries - Game Restart and Score Update
    if ball.xcor() > 350:
        score_o += 1
        score.clear()
        score.write("Player: {}  Opponent: {}".format(score_p, score_o), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = random.choice([-1, 1])*ball.dx
    
    if ball.xcor() < -350:
        score_p += 1
        score.clear()
        score.write("Player: {}  Opponent: {}".format(score_p, score_o), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = random.choice([-1, 1])*ball.dx
    
    # Collisions
    if ball.xcor() > 340 and ball.ycor() < player_paddle.ycor() + 50 and ball.ycor() > player_paddle.ycor() -50:
        ball.setx(340)
        ball.dx *= -1
        
    if ball.xcor() < -340 and ball.ycor() < opponent_paddle.ycor() + 50 and ball.ycor() > opponent_paddle.ycor() -50:
        ball.setx(-340)
        ball.dx *= -1