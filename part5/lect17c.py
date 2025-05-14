import json
import pandas as pd

students_df = pd.read_json("./part5/students.json")
students_df.Age  = students_df.Age +1 #group of preproccing and cleaning
students_df.to_json("./part5/students_cleaned.json",orient='records')
print(students_df)
