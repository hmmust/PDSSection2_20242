import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(students_df.isnull())
#print(students_df.notnull())
print(students_df.isnull().sum())
print(students_df.info())
print(students_df.Year.value_counts(dropna=False))
print(students_df.Year.isnull().sum())




