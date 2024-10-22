import numpy as np

a = np.arange(0,18).reshape((6,3))
b = np.arange(20,38).reshape((6,3))
print(a)
print(b)

print(a+b)
print(np.add(a,b))

print(a-b)

print(a*b)

print(a/b)
np.multiply(a,b)


b = b.reshape(3,6)
print(a@b)

print(a.dot(b))

print(a.max())
print(b.max())

print(b.argmax())

print(np.sum(b))

#will give sum for each row
print(np.sum(b,axis=1))
print(np.sum(b,axis=0))
print(np.mean(b))
print(np.sqrt(b))
print(np.std(b))
print(np.log(b))


