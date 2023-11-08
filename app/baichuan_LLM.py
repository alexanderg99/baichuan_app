from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

class Model:

    def __init__(self):
        pass

    def load_model():
        model = AutoModelForCausalLM.from_pretrained("./models/Baichuan2/")
        model.generation_config = GenerationConfig.from_pretrained("baichuan-inc/Baichuan2-13B-Chat")
        

        return model
    
    def load_tokenizer():
        tokenizer = AutoTokenizer.from_pretrained("./models/Baichuan2/")
        return tokenizer