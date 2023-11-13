from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

class Model:

    def __init__(self):
        pass

    def load_model():
        model = AutoModelForCausalLM.from_pretrained("./models/Baichuan2/",load_in_8bit=True, device_map="cuda:0", trust_remote_code=True)
        model.generation_config = GenerationConfig.from_pretrained("./models/Baichuan2")
        

        return model
    
    def load_tokenizer():
        tokenizer = AutoTokenizer.from_pretrained("./models/Baichuan2/",trust_remote_code=True)
        return tokenizer
