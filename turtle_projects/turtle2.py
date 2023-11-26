from turtle import Turtle, Screen
import random

# colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'orange red', 'LightSeaGreen', 'SlateGray', 'SeaGreen']
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270]
new = Turtle()
new.pensize(15)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =(r, g, b)
    return random_color


def move():
    for i in range(200):
        new.speed('fastest')
        new.forward(30)
        new.setheading(random.choice(directions))
        new.color(random_colors())
        
move()



screen.exitonclick()