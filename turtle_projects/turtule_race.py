from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title='Make a Bet', prompt='Which turtle will win the race? Choose a color: ')
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'maroon']
all_turtles = []
n = 40
for i in range(6):
    new = Turtle(shape='turtle')
    new.color(colors[i])
    new.penup()
    new.goto(x=-230, y=((-60) - n))
    n = n - 40
    all_turtles.append(new)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} is the winner.")
            else:
                print(f"You lost! The {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()



