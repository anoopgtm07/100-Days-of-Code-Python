from turtle import Turtle, Screen
import random

new = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor('black')

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =(r, g, b)
    return random_color

new.speed('fastest')

for i in range(100):
    new.color(random_colors())
    new.circle(100)
    new.setheading(new.heading() + 10) 
    

screen.exitonclick()