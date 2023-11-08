

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
import uvicorn
import logging
from chatbot import Chatbot


app = FastAPI()
router = APIRouter()
#templates = Jinja2Templates(directory="templates")
baichuan=Chatbot()



@app.get("/")
async def read_root():
    return {"message": "Deployment is possible."}


@app.post("/chat")
async def chat(data: dict) -> dict:
    try:
         input_text = data["text"]
         response = Chatbot.chat(input_text)

    except Exception as e:
         logging.log.error("Retry")



    return {"response": response}

if __name__ == "__main__":
      uvicorn.run("app:app", reload=True, port=6000, host="0.0.0.0")