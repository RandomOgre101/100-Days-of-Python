# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('CadetBlue')
# timmy.forward(100)
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Charmander", "Pikachu", "Squirtle"])
table.add_column("Type", ["Fire", "Electric", "Water"])
table.align = "l"
print(table)

