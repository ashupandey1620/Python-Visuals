import numpy as np

print(np.random.random(1))

print(np.random.random(2))

print(np.random.random((2,2)))

#Randomly Generated Integer
print(np.random.randint(1,10))

#randomly generated Integer in the
# range (1-10) and matrix size (2,2)
print(np.random.randint(1,10,(2,2)))

# 3d Array
print(np.random.randint(1,10,(3,4,5)))

#only the positive values are generated
print(np.random.rand(2,2))

#genrate both negative and positive values
print(np.random.randn(2,2))

a = np.arange(1,10)
print(a)

print(np.random.choice(a))
