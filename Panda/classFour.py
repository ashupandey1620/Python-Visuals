import pandas as pd

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv')
print(df.head())

# check null values by using function df.isnull()
print(df.isnull())
# if any value will be null then the matrix will be marker True at its position

print(df.isnull().sum())

print(df.isnull().sum().sum())

#All the rows that are consisting of at least one null values need to be eliminated
print(df.shape)


#Droping ROWS with Null Values
df2 = df.dropna()
print(df2.shape)
print(df2)

#Dropping COLUMNS with Null Values
df3 = df.dropna(axis=1)
print(df3.shape)
print(df3)

#if any row value is null then remove that row
print(df.dropna(how = 'any'))

#if all value are null then remove that row
print(df.dropna(how = 'all'))

#but df.dropna(inplace = True)
df.dropna(inplace = True)
print(df.shape)
#It saves the space by changing the
#Dataframe in place and we do not need to copy the dataframe


