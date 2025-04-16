import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
del students_df['GPA']
students_df.pop('Major')

students_df['University'] = 'UOP'
students_df['BirthYear'] = 2025- students_df['Age']
students_df['FirstName'] = [ n.split()[0]  
                            for n in students_df['Name'] ]
students_df['LastName'] = students_df['Name'].str.split(' ').str[1]

print(students_df)