import json
import pandas as pd
with open("./part5/students.json",mode='r') as file1:
      students_data = json.load(file1)
print(students_data,type(students_data))
print(students_data[0]['name'])
student_df= pd.DataFrame(students_data)
print(student_df)