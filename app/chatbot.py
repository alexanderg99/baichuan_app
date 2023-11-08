from baichuan_LLM import Model
import numpy as np

class Chatbot:
    def __init__(self):
        self.model = Model.load_model()
        self.tokenizer = Model.load_tokenizer()

    def chat(self, prompt=str):
        messages = []
        messages.append({"role": "user", "content": prompt})
        response = self.model.chat(self.tokenizer, messages)
        return response