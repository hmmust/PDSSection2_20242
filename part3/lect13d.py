import pandas as pd
import numpy as np
students_df = pd.read_csv('./part3/students.csv')
print(type(students_df['Name']))

students_df['Firstname']= [ n.split()[0] for n in students_df['Name']]
students_df['Lastname']= [ n.split()[1] for n in students_df['Name']]
students_df['Shift']= np.random.randint(1,13,size=12)

students_df['Firstname']= students_df['Name'].str.split(' ').str[0].str.lower()
students_df['Lastname']= students_df['Name'].str.split(' ').str[1].str.lower()
students_df['Name']= students_df['Name'].str.replace(" ","")

print(students_df)

