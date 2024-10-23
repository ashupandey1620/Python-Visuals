import seaborn as sns

#for Bar Plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL.ImageColor import colormap

df = sns.load_dataset('titanic')
print(df.head())

sns.barplot(x='class',y='fare',data = df)
plt.show()

sns.barplot(x='class',y='fare',data = df,hue='sex')
plt.show()

sns.barplot(x='class',y='fare',data = df,hue='sex',palette='inferno')
plt.show()

sns.barplot(x='class',y='fare',data = df,hue='sex',palette='icefire')
plt.show()

sns.barplot(x='class',y='fare',
            data = df,hue='sex',
            palette='icefire', estimator=np.median)
plt.show()


#confidence-interval
sns.barplot(x='class',y='fare',
            data = df,hue='sex',
            palette='inferno',
            ci=100,
            errcolor='red',
            err_kws={'linewidth': 10})
plt.show()


# Saturation Means() less the saturation of a color more it is near to black and white
sns.barplot(x='class',y='fare',
            data = df,hue='sex',
            palette='inferno',
            saturation=0.1)
plt.show()