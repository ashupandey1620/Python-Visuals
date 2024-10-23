import pandas as pd

# loc() and iloc() in pandas

# loc() = location
# iloc() = indexlocation

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv',index_col=['Roll No.'])
print(df.head())
print(df.loc[1])
print(df.loc[[1,2,3,4]])

print(df.loc[5,'Physics'])

print(df.loc[5:15,'Chemistry'])


# I can also select the dataset using this,

print(df.loc[df['Physics']>80])


# When I want to see the maths marks for those students
# who got more than 80 in physics
print(df.loc[df['Physics']>80,['Maths']])


#Now the iloc()


#It will not take roll num as the index that I have set up
#but it will take the normal roll num that is already there
print(df.iloc[0])
print(df.iloc[[5,6,7,8]])



# If I want to see all the rows of the ith+1 column
print(df.iloc[:, 0])

print(df.iloc[:, 1])

print(df.iloc[0:5,1:4])













