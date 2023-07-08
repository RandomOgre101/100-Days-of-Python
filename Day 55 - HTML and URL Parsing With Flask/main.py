def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper
 
 
def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper 

colors = ['blue', 'red', 'purple', 'green', 'yellow', 'pink']

from flask import Flask
import random

app = Flask(__name__)

crct = random.randint(0,9)

@app.route('/')
@make_bold
def landing_page():
    return f'<h1 style="color:{random.choice(colors)}">Choose a number betwen 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/oBQZIgNobc7ewVWvCd/giphy-downsized-large.gif">'

@app.route('/<int:num>')
def number(num):
    if num == crct:
        return  f'<h1 style="color:{random.choice(colors)}">CORRECT!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num > crct:
        return f'<h1 style="color:{random.choice(colors)}">Too high! Guess again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h1 style="color:{random.choice(colors)}">Too low! Guess again</h1>'\
                '<img src=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
