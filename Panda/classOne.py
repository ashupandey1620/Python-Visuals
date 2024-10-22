import pandas as pd

lst = [1,2,3,4,5]
print(lst)

series = pd.Series(lst)
print(series)
print(type(series))


empty = pd.Series([])
print(empty)


#Defining your own indexes
a = pd.Series(['p','q','r','s','t'], index=[10,11,12,13,14])
print(a)

a = pd.Series(['p','q','r','s','t'], index=[10,11,12,13,14], name="alphabets")
print(a)

#can also provide the scalar values
scalar_series = pd.Series(0.5)
print(scalar_series)

#can also provide the multiple scalar values
scalar_series = pd.Series(0.5, index=[1,2,3,4])
print(scalar_series)

#All these were using a panda Series using a List
#Now we will se it implementing using a Python Dictionary

dict_series = pd.Series({
    'p':1,
    'q':2,
    'r':3,
    's':4,
    't':5
})
print(dict_series)


print(dict_series[0])
print(dict_series[0:3])

print(max(dict_series))


dict_series = pd.Series({
    'p':[1,5,6],
    'q':[2,6,7],
    'r':[3,9,0],
    's':[4,4,3]
})

print(dict_series)



