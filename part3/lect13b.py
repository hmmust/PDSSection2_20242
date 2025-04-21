import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(students_df.sum())
age_sum = students_df['Age'].sum()
print(age_sum)
print(students_df.Age.sum())

print(students_df.count())
print(students_df.loc[:,['Age','GPA','Year']].mean())
print(students_df.loc[:,['Age','GPA','Year']].median())
print(students_df.loc[:,['Age','GPA','Year']].max())
print(students_df.loc[:,['Age','GPA','Year']].min())

print(students_df.Year.value_counts(dropna=False))
print(students_df.Major.value_counts(dropna=False))

