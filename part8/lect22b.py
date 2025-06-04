import requests
import pandas as pd 

new_student = {"id":20299,"name":"Layan Kawash",
               "age":21,"major":"DS",#"year":2022,
               "gpa":3.8}
local_url = "http://127.0.0.1:8000/students/add/"
result = requests.post(url=local_url,json=new_student)
if result:
    print(result.text,result.status_code)
    print("student added!")
else:
    print(result.text,result.status_code)
    print("Invalid student data!")