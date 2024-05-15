import pandas as pd
#
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# list_of_fur_color = data["Primary Fur Color"]
# #
# # counts = data['Primary Fur Color'].value_counts()
# # print(counts)
# #
# # counts.reset_index().to_csv('squirrel_count.csv')

# Another Method
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
