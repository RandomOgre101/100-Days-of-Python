import turtle
import pandas as pd

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")

all_states = df.state.to_list()

correct_guesses = []
score = 0
while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer in all_states and answer not in correct_guesses:
        score += 1
        correct_guesses.append(answer)
        pen = turtle.Turtle()
        pen.speed("fastest")
        pen.hideturtle()
        pen.color("black")
        pen.penup()
        pen.goto(x=int(df[df.state == answer]["x"]), y=int(df[df.state == answer]["y"]))
        pen.write(f"{answer}", align="left", font=FONT)

    elif answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        missing = pd.DataFrame(missing_states)
        missing.to_csv("states_to_learn.csv")
        break





