import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(students_df[ (students_df['Major'] == 'DS')  
      &  (students_df['GPA'] >= 3.0)])
print(students_df[ (students_df['Major'] == 'DS')  
      |  (students_df['Major'] == 'CS')])
print(students_df[ (students_df['Major'].isin(['DS','CS']))])
print(students_df[ ~(students_df['Major'].isin(['DS','CS']))])