import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#students_df.dropna(inplace=True)
students_df.dropna(axis=1,inplace=True)

#students_df= students_df.dropna(inplace=True)
print(students_df)




