from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional


import uvicorn
import logging

app = FastAPI()
router = APIRouter()

class Query(BaseModel):
    query: str
    


@app.get("/")
async def read_root():
    return {"message": "Deployment is possible."}


@app.post("/chat")
async def chat(data: Query):
    
    input_text = data.query
    response = f"I Have Heard Your Question. You asked {input_text}"
    return {"response":response}

if __name__ == "__main__":
      uvicorn.run("test_inference:app", reload=True, port=8000, host="0.0.0.0")
      