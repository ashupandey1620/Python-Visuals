import numpy as np

list = [1,2,3,4,5]
print(list)


print('1D Array')
a = np.array([1,2,3,4,5])
print(a)

print('2D Array')
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)

print('3D Array')
c = np.array([[[1,2,3,4,5],[6,7,8,9,10],[1,2,3,3,4]]])
print(c)

print('Float type Data')
d = np.array([[1,2,3,4.5,5],[6,7,8,9,10]])
print(d)

print(type(a))

print(a.size)
print(b.size)
print(c.size)

#shape = (rows,columns)
print(a.shape)
print(b.shape)
print(c.shape)

#dtype = Type of Data present in the array
print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d.dtype)


print(d.transpose())