
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Deployment is possible."}


@app.post("/predict/")
def predict():
    return {"foo": "Hello"}