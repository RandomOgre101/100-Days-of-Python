from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Turtle Race Bet", prompt="Which turtle will win the race?\nEnter a colour ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20,  20 ,60, 100]
turtles = []
cont = False

for turtle in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colours[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_pos[turtle])
    turtles.append(new_turtle)

if bet:
    cont = True
    while cont:
        for turtle in turtles:
            if turtle.xcor() > 230:
                cont = False
                winning_colour = turtle.pencolor()
                if winning_colour == bet:
                    print(f"\nCongratulations! {winning_colour} won!")
                else:
                    print(f"\nCommiserations. {winning_colour} won.")

            else:
                dist = random.randint(10,20)
                turtle.forward(dist)


screen.exitonclick()