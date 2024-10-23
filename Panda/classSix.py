
import pandas as pd


#For replace function

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv')
print(df.head())

print(df.replace(to_replace=56,value=30))
# there is no problem with the decimal and int value in this.

print(df.replace(56,1000))


#can define the list in the to_replace for replacing all the num in the list
print(df.replace(to_replace=[52,53,54,55,56],value = 'A'))


#we can also replace in this format as the key value pair
print(df.replace(to_replace=[50,51,52,53],value = ['A','B','C','D']))


print(df.replace('[A-Za-z]',0,regex=True))

#filling the backward fill while replacing it
print(df.replace(to_replace=23, method = 'ffill'))

