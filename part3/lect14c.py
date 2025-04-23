import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#students_df.Year.fillna(2015,inplace=True)
#students_df.Year.fillna(students_df['Year'].median()
#                        ,inplace=True)
#students_df.Year.fillna(students_df['Year'].mean()
#                        ,inplace=True)
#students_df.Year.fillna(method='pad',inplace=True)
students_df.Year.fillna(method='backfill',inplace=True)
#students_df.Year.ffill(inplace=True)
#students_df.Year.bfill(inplace=True)

print(students_df)





