from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(text="Newer Text")

def button_clicked():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row = 0)


input = Entry(width=10)
input.grid(column=3, row=2)

# def add(*args):
#     sum = 0
#     for _ in args:
#         sum += _
#     return sum

# def calc(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n

# print(calc(2, add=3, multiply=5))



window.mainloop()