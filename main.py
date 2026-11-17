from fastapi import FastAPI

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
