from fastapi import FastAPI
from pydantic import BaseModel
from app.inference import summarize_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    summary = summarize_text(request.text)
    return {
        "summary": summary
    }



