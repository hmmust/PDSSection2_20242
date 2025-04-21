import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
students_df['BirthYear'] = 2025- students_df['Age']

print(students_df['BirthYear'].cov(students_df['Age']))
print(students_df['BirthYear'].corr(students_df['Age']))
print(students_df['Age'].corr(students_df['BirthYear']))
print(students_df.rank())
print(students_df.rank(method='dense',ascending=False))
print(students_df)


