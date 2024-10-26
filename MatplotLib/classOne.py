import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

roll_no = [1,2,3,4,5,6,7,8]
marks = [10,20,30,40,50,60,70,80]

# Scatter plot
plt.scatter(roll_no,marks)
plt.show()

# //changing the color
plt.scatter(roll_no,marks,color = 'green')
plt.show()

# changing the marker content
plt.scatter(roll_no,marks,color = 'blue',marker = 'v')
plt.show()

plt.figure(figsize=(12,6))
plt.scatter(roll_no,marks,color = 'green')
plt.show()

plt.figure(figsize=(8,8))
plt.plot(roll_no,marks,'bo',markersize = 20)
plt.show()
# Blue means color o means circle

plt.figure(figsize=(8,8))
plt.plot(roll_no,marks,'gv',markersize = 30)
plt.show()

temp_pune = [25,34,21,45,28,6,42,18,7,2]
humid_pune = [28,25,29,20,26,50,19,29,52,55]

temp_bang = [34,35,36,37,28,27,26,25,31,20]
humid_bang =[40,38,36,35,42,44,41,40,34,45]

plt.figure(figsize=(8,8))
plt.plot(temp_pune,humid_pune,'ro',markersize = 20)
plt.show()



plt.figure(figsize=(8,8))
plt.xticks(np.arange(0,60,5))
plt.yticks(np.arange(10,60,5))

plt.plot(temp_pune,humid_pune,'ro',markersize = 10)
plt.plot(temp_bang,humid_bang,'bo',markersize = 10)
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.show()


df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\IRIS.csv')
print(df.head())


plt.plot(df['sepal_length'],df['petal_length'],'ro')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()











