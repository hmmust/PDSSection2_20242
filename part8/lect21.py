from fastapi import FastAPI,HTTPException
import pandas as pd
import json
app = FastAPI()
student_df = pd.read_json("./students.json",orient="columns")
student_df.major.replace({"DSS":"DS"," SE":"SE"},inplace=True)

@app.get('/majors/')
def get_majors():
    return list(student_df.major.unique())

@app.get('/students/major/{major}')
def get_major_students(major):
    return json.loads(student_df[student_df.major == major].to_json())


@app.get('/students/{id}')
def get_students(id:int):
    #id = int(id)
    student= student_df[student_df.id == id]
    if  len(student)==1:
        return json.loads(student.to_json())
    else:
        raise HTTPException(status_code=404,
                            detail="Student not found!")

@app.get('/students/delete/{id}')
def get_delete_students(id:int):
    #id = int(id)
    student= student_df[student_df.id == id]
    if  len(student)==1:
        student_df.drop(student_df[student_df.id == id].index,
                inplace=True,axis=0)
        student_df.reset_index(inplace=True)
        student_df.to_json("./students.json",orient="columns")
        #return {"message":"student deleted "+ id}
        raise HTTPException(status_code=200,
                            detail=f"student deleted {id}")
    else:
        raise HTTPException(status_code=404,
                            detail="Student not found!")