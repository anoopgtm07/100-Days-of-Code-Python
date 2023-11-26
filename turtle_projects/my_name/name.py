from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1000, height=700)
name = Turtle()


def index():
    name.penup()
    name.goto(x=0, y= 100)
    name.pendown()
    name.setheading(0)
    name.forward(500)
    name.backward(1000)
    name.penup()
    name.goto(x=0, y = -100)
    name.pendown()
    name.setheading(0)
    name.forward(500)
    name.backward(1000)

def a():
    name.penup()
    name.goto(x=-300, y=100)
    name.pendown()
    name.setheading(245)
    name.forward(218)
    name.backward(218)
    name.setheading(295)
    name.forward(218)
    name.backward(109)
    name.setheading(180)
    name.forward(93)


def n():
    name.penup()
    name.goto(x=-150, y=100)
    name.pendown()
    name.setheading(270)
    name.forward(200)
    name.backward(200)
    name.setheading(300)
    name.forward(230)
    name.setheading(90)
    name.forward(200)

def u():
    name.penup()
    name.goto(x=50, y=100)
    name.pendown()
    name.setheading(270)
    name.forward(150)
    name.circle(50, 170)
    name.setheading(90)
    name.forward(160)

def p():
    name.penup()
    name.goto(x=220, y= 100)
    name.pendown()
    name.setheading(270)
    name.forward(200)
    name.backward(100)
    name.setheading(0)
    name.circle(50, 180)

name.speed('fast')
name.pensize(5)
name.color('red')
a()
n()
u()
p()
index()
screen.bgcolor('black')
screen.exitonclick()
