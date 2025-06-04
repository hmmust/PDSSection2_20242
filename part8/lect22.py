from fastapi import FastAPI,HTTPException
import pandas as pd
from pydantic import BaseModel
import json
app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    age:int
    major:str
    year:int = None
    gpa:float
@app.post('/students/add/')
def post_new_student(student:Student):
    student_df = pd.read_json("./students.json",orient="columns")
    student_df.major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
    new_student_df = pd.DataFrame([student.dict()])
    student_df = pd.concat([student_df,new_student_df],
                           axis=0,ignore_index=True)
    student_df.to_json("./students.json")
   
    return {"detail":"Student added succefully!"}
    #raise HTTPException(status_code=200,
    #                    detail="Student added succefully!")