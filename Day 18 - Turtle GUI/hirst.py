import colorgram
from turtle import *
import random

# colors1 = colorgram.extract('hirst.webp', 10)

# colours = []

# for color in colors1:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g,b)
#     colours.append(new_colour)

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed("fastest")
colour_list = [(56, 108, 149), (226, 132, 55), (197, 145, 172), (234, 201, 101), (145, 81, 54), (140, 180, 207), (233, 225, 195), (138, 130, 73)]


def paint():
    for i in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()


y_val = -300
for i in range(10):
    timmy.penup()
    timmy.setpos(-300,y_val)
    timmy.pendown()
    y_val += 50
    paint()


screen.exitonclick()