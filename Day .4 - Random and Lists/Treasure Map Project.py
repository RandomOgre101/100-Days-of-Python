# Treasure Map

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

rowmap = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input('Where would you like to place the treasure?: ')

horizontal = int(position[0])
vertical = int(position[1])


selectedRow = rowmap[vertical - 1]
selectedRow[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")







