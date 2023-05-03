from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def move_left():
    tim.rt(20)

def move_right():
    tim.lt(20)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()