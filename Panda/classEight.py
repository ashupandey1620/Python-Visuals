import pandas as pd

# Groupby() and merge()
df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\sample2.csv')
print(df.head())

branch_group = df.groupby(by = 'Branch')
print(branch_group)

# print(branch_group.groups)
# {'CS': [0, 4, 6, 9, 11, 12, 13, 26, 27, 28, 29], 'ECE': [1, 5, 8, 10, 14, 18, 22, 25], 'MECH': [2, 3, 16, 17, 19, 20, 21, 23, 24]}
# It will be quite easy as u get to know that student present in this branch is present in particular index

branch_group = df.groupby(by = ['Branch','Section'])
print(branch_group.groups)
#{('CS', 'A'): [0, 4, 9, 12, 13, 28, 29], ('CS', 'B'): [6, 26], ('CS', 'C'): [11, 27], ('ECE', 'A'): [1, 5, 8, 25], ('ECE', 'B'): [10, 14, 18, 22], ('MECH', 'A'): [16, 17, 20, 21, 24], ('MECH', 'B'): [2], ('MECH', 'C'): [3, 19, 23], (nan, 'C'): [7, 15]}
# It simplifies most of the problem as it gives all the info related to the index that which thing is present over where.

# If you want to see the data in a more clear way then
for group, data_frame in branch_group:
    print(group)
    print(data_frame)

# Merge function from here

#creating my own data Frame and not using any csv file

df1 = pd.DataFrame(
    {
        'Roll No.':[1,2,3,4],
        'Physics': [35,24,56,42]
    }
)

df2 = pd.DataFrame(
    {
        'Roll No.':[1,2,3,4],
        'Chemistry':[78,33,39,81]
    }
)

print(df1)
print(df2)

print(pd.merge(df1,df2, on='Roll No.'))

print(pd.merge(df2,df1, on='Roll No.'))

#if not providing the on parameter then the intersection column will be taken
print(pd.merge(df,df2))



# TAKING ANOTHER EXAMPLE
df3 = pd.DataFrame({
    'Roll No.':[1,2,3,6,7],
    'Physics':[34,56,64,34,54]
})

df4 = pd.DataFrame({
    'Roll No.': [1,2,3,4,5],
    'Chemistry':[78,54,65,4,45]
})

# Only that data frame will be created that do not have
print(pd.merge(df3,df4))

#but if i want to include all the params from left dataframe then I can put it in the syntax
print(pd.merge(df4,df3,how='left'))

# out will take all the numbers
print(pd.merge(df4,df3,how='outer'))



