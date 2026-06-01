from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.chatbot import ask_question

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_question(request.question)
    return {"answer": answer}
