import pandas as pd

#Reading Dataframes as CSV(Common Separated Values)
df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\Salary_Data.csv')
print(df)

print(df.columns)
# Index(['YearsExperience', 'Salary'], dtype='object')

print(df.shape)
# (30, 2)

print(df.size)
# 60

# head() gives you the first five rows
print(df.head())

print(df.head(2))

# tail() gives you the last Five rows
print(df.tail())
print(df.tail(3))


# describe() : It gives the description of the numerical data
print(df.describe())


# info() :
print(df.info())

#Complex CSV FIle Structure
df2 = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\Restaurant.csv')

print(df2.head())
print(df2.shape)
print(df2.info())

#Give us the description of the numeric data
print(df2.describe())

