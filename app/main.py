

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.templating import Jinja2Templates

#import torch
#from transformers import AutoModelForCausalLM, AutoTokenizer
#from transformers.generation.utils import GenerationConfig


app = FastAPI()
#templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root():
    return {"message": "Deployment is possible."}


@app.post("/predict")
async def predict(input_text: str):

    tokenizer = AutoTokenizer.from_pretrained("../Baichuan2-13B-Chat", use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("../Baichuan2-13B-Chat", device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
    model.generation_config = GenerationConfig.from_pretrained("baichuan-inc/Baichuan2-13B-Chat")
    messages = []
    messages.append({"role": "user", "content": "解释一下“温故而知新”"})
    response = model.chat(tokenizer, messages)
    print(response)

    return {"response": "Hello"}

@app.post("/process_text")
async def process_text(input_text: str):

    generated_response = f"LLM generated response for: {input_text}"
    return {"result": generated_response}