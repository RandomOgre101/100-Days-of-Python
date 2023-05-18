# Mile to Kilometre Project

from tkinter import *

window = Tk()
window.title("Miles to Kilometres Converter")
window.config(padx=20, pady=20)

def calculate():
    n = float(miles_input.get())
    conv = round(n*1.609)
    km.config(text=f"{conv}")



miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc = Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)


window.mainloop()