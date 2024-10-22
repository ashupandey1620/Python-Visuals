import numpy as np

# np.arange(start,end,step)
#like a for loop
#step is not compulsary to give


a = np.arange(1,20)
print(a)

b = np.arange(1,20,2)
print(b)

c = np.arange(2,20,2)
print(c)


# arr.reshape((3,3))
c = c.reshape((3,3))
print(c)

b = np.arange(1,100,2)
print(b)

b = b.reshape((5,10))
print(b)

#flatten
b = b.flatten()
print(b)

#ravel
c = c.ravel()
print(c)



#Ravel - It returns only reference/view of original array. If u modify
# the array you would notice that the value of original array also changes

# Flatten - It returns the copy of original array, It modifies any
# value of this array value of the original array if not affected.


#Flatten is comparitively slower than ravel() as it occupies memory.


