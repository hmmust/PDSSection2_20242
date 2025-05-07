import pandas as pd
import numpy as np

from sklearn.preprocessing import Binarizer,LabelEncoder
from sklearn.preprocessing import OneHotEncoder

students_df = pd.read_csv('./part3/students.csv')
students_df['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)

binarizer =  Binarizer(threshold=2.99)
students_df['gpa_pass']= binarizer.fit_transform(students_df.loc[:,['GPA']])

scaler =  LabelEncoder()
print(students_df.Major.unique())
scaler.fit(['CS', 'DS', 'IS', 'SE','VR'])
students_df['major_labled']= scaler.transform(students_df['Major'])

print(students_df) 