import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#students_df = students_df.drop(0)
students_df.drop(0,inplace=True,axis=0) # delete row
#students_df.drop(['Id'],inplace=True,axis=1) # delete column
students_df.reset_index(inplace=True,drop=True)
print(students_df)