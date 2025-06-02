import requests
import pandas as pd 

local_url = "http://127.0.0.1:8000/majors/"
result = requests.get(url=local_url)

for major in result.json():
    print("Major", major, "Students:")
    local_url = "http://127.0.0.1:8000/students/major/" + major
    students_result = requests.get(url=local_url)
    students_df = pd.DataFrame(students_result.json())
    print(students_df.loc[:,['name','gpa']])