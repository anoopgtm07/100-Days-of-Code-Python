from turtle import Turtle, Screen

new = Turtle()
screen = Screen()
new.screen.bgcolor('black')
new.pensize(2)
new.color('green')

new.left(90)
new.backward(100)
new.shape('turtle')
new.speed('fastest')


def tree(i):
    if i < 10:
        return
    else:
        new.forward(i)
        new.color('orange')
        new.circle(2)
        new.color('brown')
        new.left(30)
        tree(3 * i / 4)
        new.right(60)
        tree(3 * i / 4)
        new.left(30)
        new.backward(i)


tree(100)
screen.exitonclick()
