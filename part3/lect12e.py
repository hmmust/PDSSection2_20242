import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
students_df2 = students_df[:2]
students_df3= pd.concat([students_df,students_df2],
                        ignore_index=True)
#students_df3.reset_index(inplace=True,drop=True)
print(students_df3)