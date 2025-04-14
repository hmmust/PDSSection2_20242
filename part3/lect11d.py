import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#print(students_df.Name)
print(students_df['Name'])
print(students_df[['Name','Age']])
print(students_df[0:2])
print(students_df[(students_df['Age'] >20) &(students_df['Major']=='DS')])

print(students_df[~((students_df['Age'] >20) &(students_df['Major']=='DS'))])
