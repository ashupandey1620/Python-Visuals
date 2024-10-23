import seaborn as sns

#for SCATTER PLOT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL.ImageColor import colormap

df = sns.load_dataset('titanic')
print(df.head())

sns.scatterplot(x='age',y='fare',data=df)
plt.show()

sns.scatterplot(x='age',y='fare',data=df,hue='alive')
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x='age',y='fare',data=df, hue='alive',style='class')
plt.title("Titanic Data Analysis")
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x='age',y='fare',data=df, hue='alive',style='class')
sns.lineplot(x='age',y='fare',data=df)
plt.title("Titanic Data Analysis")
plt.show()
