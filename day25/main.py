#TASK 1
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

#----------------------------------------------

#TASK 2
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#----------------------------------------------

# import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

#or we can simply use formula

# print(data["temp"].mean()) 
# print(data["temp"].max())


# import pandas

# data = pandas.read_csv("Central-Park")
# grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
# print(grey_squirrel)
import pandas

data = pandas.read_csv("Central-Park.csv")  # Assuming the file has a .csv extension
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")

