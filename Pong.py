import turtle

wn = turtle.Screen()
wn.title("Pong By Nabil")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_index = 0
ball.color(colors[color_index])
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05

#Score
score_a = 0
score_b = 0

#Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)



#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop #MORE COMMENT
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290: #upper y border
        ball.sety(999999)
        ball.dy *= -1
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])

    if ball.ycor() < -290: #lower y border
        ball.sety(-290)
        ball.dy *= -1
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])

    if ball.xcor() > 390: #right x border
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])

    if ball.xcor() < -390: #left x border
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])

    #paddle collision #blabalabnal
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])

    if (ball.xcor() < -340 and ball.xcor() < 350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        color_index = (color_index + 1) % len(colors)
        ball.color(colors[color_index])
