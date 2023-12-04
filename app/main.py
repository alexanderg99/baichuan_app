

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
import uvicorn
import logging
from chatbot import Chatbot
from pydantic import BaseModel

from fastapi.templating import Jinja2Templates

app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="templates")
baichuan=Chatbot()
class Query(BaseModel):
    query: str




@app.get("/")
async def read_root(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})

    #    return {"message": "Deployment is possible."}


@app.post("/chat")
async def chat(request: Request, data: Query):
    try:
         input_text = data.query
         response = baichuan.chat(input_text)
         return templates.TemplateResponse("index.html", {"request": request, "response": response})

    except Exception as e:
         
         logging.error(f"An exception occurred: {e}")


    return {"response": response}

if __name__ == "__main__":
      uvicorn.run("main:app",port=8000, host="0.0.0.0")
      
