import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler,StandardScaler,normalize

students_df = pd.read_csv('./part3/students.csv')
scaler1 =  MinMaxScaler(feature_range=(0,1)) 
scaler2 =  StandardScaler()

students_df['gpa_scaled']= scaler1.fit_transform(students_df.loc[:,['GPA']])
students_df['gpa_scaled2']= scaler2.fit_transform(students_df.loc[:,['GPA']])
students_df['gpa_normalized']= normalize(students_df.loc[:,['GPA']],norm='l2',axis=0 )


print(students_df) 