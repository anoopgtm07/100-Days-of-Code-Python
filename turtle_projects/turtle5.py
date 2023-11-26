from turtle import Turtle, Screen
import random

# The code below is used to extract the colors from the image using cologram module
# once the colors are extracted we can save them as tuples or list
# for this we need to have an image inside the working directory
# ------------------------------------------------------------------------------------------
# import colorgram

# colors_rgb = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb =(r, g, b)
#     colors_rgb.append(new_rgb)
# print(colors_rgb)
# --------------------------------------------------------------------------------

new = Turtle()
screen = Screen()
screen.colormode(255)
new.speed('fastest')
new.penup()
new.hideturtle()

colors_list = [(226, 237, 244), (138, 173, 192), (223, 206, 119), (43, 106, 138), (139, 183, 149), (15, 52, 75),
               (218, 88, 65), (36, 126, 105), (124, 81, 95), (193, 133, 145), (71, 164, 120), (145, 81, 71),
               (12, 58, 49), (55, 153, 180), (51, 34, 43), (126, 37, 50), (205, 85, 102), (175, 206, 171), (6, 109, 87),
               (229, 168, 182), (147, 204, 230), (157, 153, 67), (33, 64, 101), (16, 84, 100), (47, 30, 27),
               (184, 189, 203)]

new.setheading(225)
new.forward(300)
new.setheading(0)

num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    new.dot(20, random.choice(colors_list))
    new.forward(50)

    if dot_count % 10 == 0:
        new.setheading(90)
        new.forward(50)
        new.setheading(180)
        new.forward(500)
        new.setheading(0)

screen.exitonclick()
