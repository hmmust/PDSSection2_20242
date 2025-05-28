from fastapi import FastAPI
app = FastAPI()
# get /
@app.get('/')
def get_data():
    return {'name':'hossam mustafa'}

@app.get('/age/')
def get_age():
    return {'age':21}