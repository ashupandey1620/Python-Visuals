

#Line chart
# Seaborn is a python data visualisation library based on matplotlib.
# It provides a high-level interface for drawing attractive and informative statistical graphics.
import seaborn as sns

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

roll_no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks = [23,45,67,89,56,34,21,45,67,32,67,76,33,21,45]
sample_df = pd.DataFrame({
    'Roll_No': roll_no,
    'Marks': marks
})
print(sample_df.head())

print(sns.lineplot(x='Roll_No', y='Marks', data=sample_df))
print(plt.title('Student Marks'))
plt.show()

seaborn_df = sns.load_dataset('planets')
print(seaborn_df.head())

sns.lineplot(x='mass',y='distance',data=seaborn_df)
plt.title('Planets Data')
plt.show()

df = pd.read_csv(r'C:\Users\ashup\OneDrive\Desktop\Sample CSV Data\hr_data.csv')
print(df.head())

sns.lineplot(x='number_project',y='average_montly_hours',data=df)
plt.title('HR Data Line Chart')
plt.show()

sns.lineplot(x='promotion_last_5years',y='left',data=df)
plt.title('Promotion Last 5 Years')
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(x='department',y='left',data=df)
plt.title('Department Last 5 Years Leave')
plt.show()

sns.lineplot(x='number_project',
             y='average_montly_hours',
             data=df,
             hue='department')
plt.title('hue Map Line Chart')
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(x='number_project',
             y='average_montly_hours',
             data=df,
             hue='left',
             style='department',
             legend=False,
             palette='flare')
plt.title('hue Map Line Chart')
plt.show()















