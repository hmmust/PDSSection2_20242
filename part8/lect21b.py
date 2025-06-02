import pandas as pd
import json
student_df = pd.read_json("./part8/students.json",orient="columns")
student_df.major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
print(list(student_df.major.unique()))
print(list(set(student_df.major)))

major = 'DS'
print(json.loads(student_df[student_df.major == major].to_json()))

id = 20209
print(json.loads(student_df[student_df.id == id].to_json()))
print(student_df[student_df.id == id].index)
student_df.drop(student_df[student_df.id == id].index,
                inplace=True,axis=0)
student_df.reset_index(inplace=True)
print(student_df)