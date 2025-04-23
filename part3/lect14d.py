import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
#students_df.Year.fillna(method='backfill',inplace=True)
students_df.Year.replace({np.nan:2015},inplace=True)
students_df.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
students_df.Year=students_df.Year.astype(np.int16)
students_df.Age=students_df.Age.astype(np.int16)
print(students_df.dtypes)





