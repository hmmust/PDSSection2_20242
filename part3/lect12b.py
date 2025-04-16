import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(students_df.loc[0,'Name'])
print(students_df.loc[[0,1],'Name'])
print(students_df.loc[[0,1],['Name','GPA']])
print(students_df.loc[0:3,['Name','GPA']])
print(students_df.iloc[0,1])
print(students_df.iloc[[0,1],1])
print(students_df.iloc[[0,1],[1,5]])
print(students_df.iloc[0:3,[1,5]])
print(students_df.iloc[:,:-1]) # x training dataset
print(students_df.iloc[:,-1:]) # y training dataset