import pandas as pd
from pandas import DataFrame

# Dataframe is the collection of data that contains rows and columns

df = pd.DataFrame()
print(df)

#we can create the dataframes manually and I can also create dataframe using csv or xlsv files


#USING LIST
lst = [1,2,3,4,5]
df = pd.DataFrame(lst)
print(df)

lst = [[1,2,3,4,5],[11,12,13,14,15]]
df = pd.DataFrame(lst)
print(df)


#Dictionary Keys represents your column name
a = [{'a':5,'b':6,'c':7,'d':8},
     {'a':4, 'b':8 , 'c': 19, 'd':12}]
df = pd.DataFrame(a)
print(df)

#Creating a dataframe using Panda Series
b = {'RollNo': pd.Series([1, 2, 3, 4, 5]),
     'Maths': pd.Series([67,91,88,75,66]),
     'Physics': pd.Series([12,98,44,90,78])}
df = pd.DataFrame(b)
print(df)


#Reading Dataframes as CSV(Common Separated Values)
df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\Salary_Data.csv')
print(df)
print(type(df))



