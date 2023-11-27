from turtle import Turtle, Screen

new = Turtle()
screen = Screen()


def move_forward():
    new.forward(30)


def move_backward():
    new.backward(30)


def right():
    new_heading = (new.heading() + 10)
    new.setheading(new_heading)


def left():
    new_heading = (new.heading() - 10)
    new.setheading(new_heading)


def clear_screen():
    new.clear()
    new.penup()
    new.home()
    new.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='a', fun=left)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()
