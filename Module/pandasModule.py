import pandas as pd
import matplotlib.pyplot as plt

# Pandas methods
# Creating data columns in pandas
print("Series")
Nums = [1, 3, 5, 7, 9]
print(pd.Series(Nums))
print(pd.Series(Nums)[1:4])
# Changing items' labels
print(pd.Series(Nums, index=["A", "B", "C", "D", "E"]))
# Creating key/value pandas objects
print("Key/Value object")
Team = {
    "Member1": "Dia",
    "Member2": "SicKickForm",
    "Member3": "akaTeen"}
print(pd.Series(Team))
# Returns specified labels
print(pd.Series(Team, index=["Member1", "Member3"]))
# Creating 2-dimensional data
print("DataFrame")
Team = {
    "Name": ["Dia", "SicKickForm", "akaTeen"],
    "Age": [17, 18, 22]}
print(pd.DataFrame(Team, index=["Member1", "Member2", "Member3"]))
# Returns specified rows
print(pd.DataFrame(Team).loc[0:1])
# One way to store big data sets is using JSON
# JSON is an object similar to dictionaries containing plain data
print("read_json")
print(pd.read_json("https://www.w3schools.com/python/pandas/data.js"))
# Comma separated file (CSV) is another simple way to store big data sets
print("read_csv")
Data = pd.read_csv("https://www.w3schools.com/python/pandas/dirtydata.csv.txt")
print(Data)
# The maximum amount of rows is defined in Pandas option settings
print("pd.options.display.max_rows")
print(pd.options.display.max_rows)
# You can change this number to remove the limit
pd.options.display.max_rows = 100
print(pd.options.display.max_rows)
# Returns headers and specified amount of rows from top (5 by default)
print("head")
print(Data.head(10))
# Returns headers and specified amount of rows from buttom (5 by default)
print("tail")
print(Data.tail(10))
# Returns information about data set
# The non-null number shows the rows with value in that header
# Rows without value in a header are bad for analysis and should be cleaned
print("info")
print(Data.info())
# Data cleaning
# Empty cells, Data in wrong format, Wrong data and Duplicates are bad data
# Cleaning empty cells
# Removing rows with empty cells in a new data set
# Use inplace=True statement to remove rows from original data set
print("dropna")
print(Data.dropna())
# Filling empty cells with given value in a new data set
# Use inplace=True statement to fill empty cells with given value in original data set
print("fillna")
print(Data.fillna(130))
# Filling empty cells of specified column with given value
print(Data["Calories"].fillna(130))
# Calculates the average of all values
print("mean")
Mean = Data["Calories"].mean()
print(Data["Calories"].fillna(Mean, inplace=True))
# Returns the center number after sorting the values ascending
print("median")
print(Data["Calories"].median())
# Returns the most frequent value
print("mode")
print(Data["Calories"].mode())
# Cleaning Data in wrong format
# Converting all cells in a column into the same data format
print("to_datetime")
print(pd.to_datetime(Data["Date"]))
# Unconvertable rows should be removed
print("subset")
Data["Date"] = pd.to_datetime(Data["Date"])
print(Data.dropna(subset=["Date"]))
# Cleaning wrong data
# Replacing wrong data
print("loc")
Data.loc[7, "Duration"] = 45
print(Data)
# You can use loops to replace values in big data sets
for i in Data.index:
    if Data.loc[i, "Duration"] < 60:
        Data.loc[i, "Duration"] = 60
print(Data)
# Removing rows with wrong data
print("drop")
Data.drop(7, inplace=True)
print(Data)
# Cleaning duplicates
# Returns True if a row is duplicate
print("duplicated")
print(Data.duplicated())
print("drop_duplicates")
print(Data.drop_duplicates(inplace=True))
print(Data)
# Calculates the statistical relationship between columns in data set
# Correlation table number between two columns varies from -1 to +1
# In a perfect +1 Correlation both values in a row either go up or go down
# In a perfect -1 Correlation one row's value goes up and the other row's value goes down
# If number gets close to 0 (after +/- 0.6) it's not a good Correlation anymore
# Not-numeric columns will be ignored
print("corr")
Data = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv.txt")
print(Data.corr())
Data = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv.txt")
Data.plot()
plt.show()
Data.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
Data["Duration"].plot(kind='hist')
plt.show()
