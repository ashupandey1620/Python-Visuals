import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv',index_col=['Roll No.'])
print(df.head())
print(df.shape)

#what was the average marks in Chemistry?
print(df['Chemistry'].mean())

#pivot allows you to transform and reshape your data

print(df.pivot(index='DOB',
               columns='Section',
               values='Chemistry'))

