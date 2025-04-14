import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(students_df)
print(students_df.shape,students_df.ndim,students_df.size)
print(students_df.head(4)) #first 5
print(students_df.tail()) #last 5
print(students_df.dtypes)
print(students_df.info())
print(students_df.describe())
print(students_df.describe(include=['object']))
print(students_df.Age.mean())
print(students_df.Major.unique())