import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
courses_df = pd.read_csv('./part3/students_courses.csv')

student_courses = pd.merge(students_df,courses_df, 
                           on=['Id']) #inner join
student_courses = pd.merge(students_df,courses_df, 
                           on=['Id'],how='left')
print(student_courses.groupby(['Id'])['Mark'].mean())
print(student_courses.groupby(['Id'])['Mark'].count())

print(pd.concat([students_df,courses_df]))
print(pd.concat([students_df,courses_df],axis=1))


