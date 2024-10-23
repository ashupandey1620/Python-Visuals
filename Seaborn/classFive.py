import seaborn as sns

#for SCATTER PLOT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL.ImageColor import colormap

df = sns.load_dataset('flights')
print(df.head())

df = df.pivot(index = "month",columns="year",values="passengers")
print(df.head())

plt.figure(figsize = (12,6))
ax = sns.heatmap(df)
plt.show()


plt.figure(figsize = (12,6))
ax = sns.heatmap(df,annot=True,fmt='d',
                 linecolor='k',linewidths='5')
plt.show()


plt.figure(figsize = (12,6))
ax = sns.heatmap(df,annot=True,fmt='d',
                 linecolor='k',linewidths='5',
                 cmap='Blues')
plt.show()


