import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#students_df = students_df.sort_index(axis=0) #sort index rows
#sort by column name
#students_df = students_df.sort_index(axis=1) 
students_df= students_df.sort_values(
    by=['Major','Age','GPA'])
students_df.sort_values(by=['Major','Age','GPA'],
                        inplace=True,ascending=False)
students_df.sort_values(by=['Major','Age','GPA'],
                        inplace=True,
                        ascending=[False,True,True])
students_df.sort_values(by=['Major','Age','GPA'],
                        inplace=True,
                        ascending=[False,True,True],
                        kind='heapsort')
print(students_df)