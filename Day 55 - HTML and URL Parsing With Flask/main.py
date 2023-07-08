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


from flask import Flask

app = Flask(__name__)

@app.route('/')
@make_bold
def landing_page():
    return '<h1 styles="color:blue">Choose a number betwen 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/oBQZIgNobc7ewVWvCd/giphy-downsized-large.gif">'

@app.route('/<int:num>')
def number(num):
    if num == 6:
        return  '<h1>CORRECT!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num > 6:
        return '<h1>Too high! Guess again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>Too low! Guess again</h1>'\
                '<img src=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
