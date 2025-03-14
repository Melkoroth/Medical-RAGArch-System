from functools import lru_cache
from transformers import AutoModel
import torch

@lru_cache(maxsize=3)  # Cachear modelos en memoria
def load_transformer_model(model_name):
    return AutoModel.from_pretrained(model_name, cache_dir=os.getenv('TRANSFORMERS_CACHE'))

@lru_cache(maxsize=3)
def load_torch_model(model_path):
    return torch.load(model_path, map_location='cpu')
