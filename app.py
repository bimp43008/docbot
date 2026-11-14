from fastapi import FastAPI
from pydantic import BaseModel
from rag_answer import rag_answer
from extract import extract
from schemas import VehicleContract

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/answer")
def answer(body: Question) -> dict:
    return{"answer": rag_answer(body.question)}

@app.post("/extract")
def extract_ep(body: Question) -> dict:
    return extract(f"Извлеки данные:\n{body.question}", VehicleContract).model_dump()