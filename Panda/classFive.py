import pandas as pd

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv')
print(df.head())

print(df.isnull().sum())
#sometimes we dont want to remove the data as it is required

print(df.fillna({
    'Physics':'none',
    'Chemistry':0,
    'Maths':23
}))
# can do for a scaler value and can also do using the map dictionary
#filling all the null values with 0


#It will the value with just the previous value
print(df.fillna(method='ffill',axis=1))
# axis = 1 column type
# axis = 0 row type

print(df.fillna(method='ffill',axis=0))




#   Now if we go more concise then we will be filling the value
#   with average of the more than 2 values

print(df['Physics'].fillna(value=df['Physics'].mean()))

print(df.fillna(method="bfill",inplace=True))







