from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag import ask_question   # IMPORTANT: no "backend." here if running inside backend

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG chatbot backend is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    return ask_question(request.question)