import numpy as np

s1 = "I am a beginnner to ML"
s2 = "I am also a Student"

print(np.char.add(s1,s2))

print(np.char.upper(s1))

print(np.char.lower(s1))

#Interesting and useful
print(np.char.split(s1))

s3 = "My name is Anthony\nGonsaalwis"
print(np.char.splitlines(s3))

print(np.char.replace(s1,"ML","Android"))


print("***********Good Bye**********")

print(np.char.center("Hello",80,"*"))

