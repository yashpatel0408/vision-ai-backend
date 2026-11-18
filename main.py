from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    exercise_name: str
    reps: int
    set: int
class UserStat(BaseModel):
    weight_kg: float
    height_m: float



app=FastAPI(title="Vision AI Backend")

@app.get("/")
def home():
    return {"message":"Day1 FastAPI server is live!"}

@app.get("/health")
def health_check():
    return {"status":"healthy","version":"1.0"}

@app.get("/exercise/{exercise_name}")
def get_exercise(exercise_name:str,reps: int = 10):
    return {"exercise":exercise_name,"target_sets":3,"reps":reps}

@app.post("/exercise/")
def create_item(exercise:Item):
    item_dict=exercise.model_dump()
    total=exercise.set*exercise.reps
    item_dict.update({"total_exercise":total})
    return item_dict

@app.post("/bmi/")
def create_item(bmi:UserStat):
    item_dict1=bmi.model_dump()
    stat=(bmi.weight_kg/(bmi.height_m**2))
    item_dict1.update({"BMI":round(stat,2)})
    return item_dict1