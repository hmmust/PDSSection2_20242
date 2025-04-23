import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
students_df.Year.replace({np.nan:2015},inplace=True)
students_df.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
students_df.Year=students_df.Year.astype(np.int16)
students_df.Age=students_df.Age.astype(np.int16)
#students_df.sort_values(by=['Major'],ascending=True,inplace=True)
students_my_df= students_df.groupby(['Major','Year'])
print(students_my_df[['Age','Year','GPA']].mean())
print(students_my_df[['Age','Year','GPA']].agg('mean'))
print(students_my_df[['Age','Year','GPA']].aggregate('mean'))
print(students_my_df[['Age','Year','GPA']].agg(np.mean))
print(students_df.groupby(['Major','Age'])['GPA'].mean())

print(students_df[ students_df['Age'] >=20].
      groupby(['Major','Year'])['GPA'].agg('count'))





