

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
import uvicorn
import logging
from chatbot import Chatbot
from pydantic import BaseModel


app = FastAPI()
router = APIRouter()
#templates = Jinja2Templates(directory="templates")
baichuan=Chatbot()
class Query(BaseModel):
    query: str




@app.get("/")
async def read_root():
    return {"message": "Deployment is possible."}


@app.post("/chat")
async def chat(data: Query):
    try:
         input_text = data.query
         response = baichuan.chat(input_text)
         

    except Exception as e:
         logging.log.error("Retry")



    return {"response": response}

if __name__ == "__main__":
      uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
