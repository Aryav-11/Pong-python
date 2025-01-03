import turtle # Imports Turtle
import random as r # Imports Random


Game_Window = turtle.Screen()
Game_Window.title("Pong Game")
Game_Window.bgcolor("black")
Game_Window.setup(width = 800, height = 600)
Game_Window.tracer(0)

# Score Counting
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3 # Moving Ball In X Direction
ball.dy = -0.3 # Moving Ball In Y Direction

# Pen For Scoring 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0          Player B: 0", align="center", font=("Retro", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
Game_Window.listen()
Game_Window.onkeypress(paddle_a_up, "w") 
Game_Window.onkeypress(paddle_a_down, "s")
Game_Window.onkeypress(paddle_b_up, "Up")
Game_Window.onkeypress(paddle_b_down, "Down")

# Main Game Loop

while True:
    Game_Window.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1 
        pen.clear()
        pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align="center", font=("Roboto", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        pen.clear()
        score_b += 1 
        pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align="center", font=("Roboto", 24, "normal"))
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        
    # Wining Thing Work
     # Player A
    if (score_a >= 5 and score_b < score_a ):
        pen.clear()
        pen.write("Player A Wins!!", align="center", font=("Roboto", 25, "bold"))
        turtle.done()
    elif (score_b >= 5 and score_a < score_b):
        pen.clear()
        pen.write("Player B Wins!!", align="center", font=("Roboto", 25, "bold"))
        turtle.done()