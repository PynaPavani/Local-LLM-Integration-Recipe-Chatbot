# pip install fastapi uvicorn transformers

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# Load fine-tuned model
model_path = "./recipe-llm"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

class Query(BaseModel):
    ingredients: str

@app.post("/chat")
def get_recipe(query: Query):
    input_text = "Ingredients: " + query.ingredients
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"ingredients": query.ingredients, "recipe": recipe}
