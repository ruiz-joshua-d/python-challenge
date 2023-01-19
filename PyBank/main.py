#Import packages
import pandas as pd

#Define filepath
file_path = "c:/users/joshu/analytics/bootcamp/myrepo/python-challenge/pybank/resources/budget_data.csv"

#Read in .csv
df = pd.read_csv(file_path)
#print (df.head(10))

#Identify total number of months included in the dataset
date_values = df["Date"].unique()
print(date_values)

#Net amount of profit/losses
net_profit = df["Profit/Losses"].sum()
print(net_profit)

row_count = df["Date"].count()
print(row_count)

#Initialize list
MyList = 0

for x in range(row_count):
    MyList = MyList + 1
    print(MyList)

