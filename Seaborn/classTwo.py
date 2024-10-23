#Hist Plot

import seaborn as sns

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\hr_data.csv')
print(df.head())
print(df.shape)


sns.histplot(df['time_spend_company'])
plt.title("Hist Plot Time")
plt.show()

sns.histplot(df['average_montly_hours'],kde=True)
plt.title("Average Monthly Hours")
plt.show()

#with bins
bins = [2,3,4,5,6,7,8,9,10]
sns.histplot(df['time_spend_company'],bins=bins,kde=True)
plt.title("Time Spend Company")
plt.show()

#without bins
sns.histplot(df['time_spend_company'],kde=True)
plt.title("Time Spend Company")
plt.show()

#bins gives us the leverage to change the range of our x column

sns.histplot(df['time_spend_company'],kde=True,rug=True)
plt.title("Time Spend Company")
plt.show()

#kws is for changing the color








