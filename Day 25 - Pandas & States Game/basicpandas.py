# with open("weather_data.csv") as file:
#     lines = file.read().splitlines()

# print(lines)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.day == 'Monday'])

# monday_temp = data[data.day == "Monday"].temp
# print((9/5)*monday_temp + 32)


# CREATING DATAFRAME FROM SCRATCH
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data =pd.DataFrame(data_dict)
data.to_csv("new_data.csv")