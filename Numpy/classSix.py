import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

plt.style.use('dark_background')

print(np.pi)

# sin 90
print(np.sin(np.pi/2))

# sin 30
print(np.sin(np.pi/2))

#It does not give u perfect value,
#It gives u a round about value

print(np.tan(np.pi/2))


#Using matPlotlib with Numpy
x = np.arange(1,11)
y = np.arange(10,110,10)

plt.figure(figsize=(6,3))
plt.plot(x,y,'r--')
plt.show()


x_sin = np.arange(0,2*np.pi,0.1)
y_sin = np.sin(x_sin)
print(y_sin)

plt.figure(figure = (6,6))
plt.plot(x_sin,y_sin)
plt.title('Sin Curve')
plt.show()


x_cos = np.arange(0,2*np.pi,0.1)
y_cos = np.cos(x_cos)
print(y_cos)

plt.figure(figure = (6,6))
plt.plot(x_cos,y_cos)
plt.title('Cos Curve')
plt.show()


x_tan = np.arange(0,2*np.pi,0.1)
y_tan = np.tan(x_tan)
print(y_tan)

x_cot = np.arange(0,2*np.pi,0.1)
y_cot = 1/np.tan(x_cot)
print(y_cot)

plt.figure(figure = (6,6))
plt.plot(x_tan,y_tan)
plt.title('Tan Curve')
plt.show()

plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
plt.plot(x_sin,y_sin,'r--')
plt.title('Sin Curve')

plt.subplot(2,2,2)
plt.plot(x_cos,y_cos,'b--')
plt.title('Cos Curve')

plt.subplot(2,2,3)
plt.plot(x_tan,y_tan,'r--')
plt.title('Tan Curve')

plt.subplot(2,2,4)
plt.plot(x_cot,y_cot,'g--')
plt.title('Cot Curve')

plt.show()







