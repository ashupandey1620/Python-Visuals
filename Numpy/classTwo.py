import numpy as np
from numpy import dtype

# np.empty((rows,cols), dtype)

a = np.empty((4,4),dtype=float)
print(a)


# np.ones((rows,columns), dtype)
x = np.ones(6)
print(x)

y = np.ones((3,5),dtype=int)
print(y)

y1 = np.ones((3,5),dtype=str)
print(y1)

y2 = np.ones((3,5),dtype=bool)
print(y2)

#np.zeros((row,column),dtype)
z = np.zeros((3,4))
print(z)

z1 = np.zeros((3,4),dtype=int)
print(z1)

z2 = np.zeros((3,4),dtype=str)
print(z2)

z3 = np.zeros((3,4),dtype=bool)
print(z3)

