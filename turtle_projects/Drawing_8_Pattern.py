from turtle import Turtle, Screen
import random

new = Turtle()

#---------------------------
# def triangle():
#     for i in range(3):
#         new.color('yellow')
#         new.forward(100)
#         new.right(120)
       
# def rectangle():
#     for i in range(4):
#         new.color('green')
#         new.forward(100)
#         new.right(90)
    
# def pentagon():
#     for i in range(5):
#         new.color('red')
#         new.forward(100)
#         new.right(72)
       
# def hexagon():
#     for i in range(6):
#         new.color('blue')
#         new.forward(100)
#         new.right(60)

# def seven():
#     for i in range(7):
#         new.color('purple')
#         new.forward(100)
#         new.right(51.42)

# def octagen():
#     for i in range(8):
#         new.color('black')
#         new.forward(100)
#         new.right(45)

# triangle()
# rectangle()
# pentagon()
# hexagon()
# seven()
# octagen()

#-----------------------------------------------------
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'orange red', 'LightSeaGreen', 'SlateGray', 'SeaGreen']

def centering_pen():
    new.penup()
    new.backward(50)
    new.left(90)
    new.forward(50)
    new.pendown()
    new.right(90)

def draw(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        new.forward(60)
        new.right(angle)

def draw_left(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        new.forward(60)
        new.left(angle)

centering_pen()
for shapes in range(3, 11):
    new.color(random.choice(colors))
    draw(shapes)

for shapes in range(3, 11):
    new.color(random.choice(colors))
    draw_left(shapes)

new_screen = Screen()
new_screen.exitonclick()
