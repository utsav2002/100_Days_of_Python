# with open("weather_data.csv", mode="r") as weather_data:
#     weather_list = weather_data.readlines()
#
# print(weather_list)
#
# import csv
#
# with open("weather_data.csv") as weather_data:
#     weather_list = csv.reader(weather_data)
#     temperatures = []
#     for row in weather_list:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas as pd

weather_data = pd.read_csv("weather_data.csv")

# print(weather_data["temp"])

# weather_data_dict = weather_data.to_dict()
# print(weather_data_dict)
#
# list_of_temp = weather_data["temp"]
# average_temp = weather_data["temp"].mean()
# print(average_temp)
#
# max = weather_data["temp"].max()
# print(max)

# Print data for Monday  ---> This goes like getting hold of the full data table, then table_name.column_name, then == xyz
# print(weather_data[weather_data.day == "Monday"])

# Printing the row with the highest temp
# print(weather_data[weather_data.temp == weather_data["temp"].max()])
# print(weather_data[weather_data.temp == weather_data.temp.max()])
#
# monday_row = weather_data[weather_data.day == "Monday"]
# print(monday_row)
#
# monday_temp = monday_row.temp[0]
# print(monday_temp)
#
# monday_temp_f = (monday_temp*(9/5)) + 32
# print(monday_temp_f)


