import pandas as pd

df = pd.read_csv('dz.csv')
print(df.info())
salary = df.groupby('City')['Salary'].mean()
print(salary)