import pandas as pd

df1 = pd.DataFrame({
    'Roll No.':[1,2,3,4,5],
    'Maths':[45,78,45,90,66],
    'Physics':[33,67,12,90,44]
})

df2 = pd.DataFrame({
    'Roll No.':[6,7,8,9,10],
    'Maths':[78,73,45,90,69],
    'Physics':[23,67,88,0,98]
})

print(df1)
print(df2)

print(df1._append(df2))
#df1 will be printed first and then df2

print(df1)
#It will not change the state of the list over here, just for the print


print(df1._append(df2,ignore_index=True))

#It is going to sort the Columns name
print(df1._append(df2,ignore_index=True,sort=True))


# Checking for the other cases:
df3 = pd.DataFrame({
    'Roll No.':[1,2,3,4,5],
    'Maths':[45,78,45,90,66],
    'Physics':[33,67,12,90,44]
})

df4 = pd.DataFrame({
    'Roll No.':[6,7,8,9,10],
    'Chemistry':[78,73,45,90,69],
    'Physics':[23,67,88,0,98]
})

print(df3)
print(df4)

print(df3._append(df2,ignore_index=True,sort=True))


#Now a case

df5 = pd.DataFrame({
    'Roll No.':[1,2,3,4,5],
    'Maths':[45,78,45,90,66],
    'Physics':[33,67,12,90,44],
    'Chemistry':[56,89,33,12,89]
})

df6 = pd.DataFrame({
    'Roll No.':[6,7,8,9,10],
    'Maths':[78,73,45,90,69],
    'Physics':[23,67,88,0,98]
})

print(df5._append(df6,ignore_index=True,sort=True))



