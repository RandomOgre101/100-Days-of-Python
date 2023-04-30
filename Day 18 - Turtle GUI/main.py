from turtle import *
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color('red', 'green')
screen = Screen()
screen.colormode(255)

## DRAWING A SQUARE
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

## DOTTED LINE
# for i in range(10):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# DRAWING SHAPES WITH SIDES 3-10
# cont = True
# sides = 3

# while cont == True:
#     for i in range(8):
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#         angle = 360/sides
#         for i in range(sides):
#             timmy.pencolor((r,g,b))
#             timmy.forward(100)
#             timmy.right(angle)
#         sides += 1
#     cont = False

## RANDOM WALK soln1 (from scratch)
# timmy.speed('fast')
# timmy.width(10)

# def choose():
#     directions = ['fd', 'bk', 'lt', 'rt']
#     choice = random.choice(directions)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

#     if choice == 'fd':
#         timmy.pencolor((r,g,b))
#         timmy.fd(30)
        
    
#     elif choice == 'bk':
#         timmy.pencolor((r,g,b))
#         timmy.bk(30)
    
#     elif choice == 'lt':
#         timmy.pencolor((r,g,b))
#         timmy.lt(90)
#         timmy.fd(30)
    
#     elif choice == 'rt':
#         timmy.pencolor((r,g,b))
#         timmy.rt(90)
#         timmy.fd(30)

# for i in range(100):
#     choose()


# RANDOM WALK soln2 using turtle functions
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")

# for i in range(200):
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     timmy.pencolor((r,g,b))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

## Spirograph
timmy.speed("fastest")

def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb


def spirograph(size):
    for i in range(int(360/size)):
        timmy.pencolor(random_rgb())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)

spirograph(5)



    
    

screen.exitonclick()