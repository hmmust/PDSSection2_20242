import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
students_df['Major']=pd.Categorical(
    students_df['Major'])#,['SE','DS','CS','IS'])
print(students_df.Major.cat.categories)
print(students_df.Major)