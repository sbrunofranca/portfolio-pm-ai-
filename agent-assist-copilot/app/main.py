# =========================================================
# IMPORTS
# =========================================================

from fastapi import FastAPI

from pydantic import BaseModel

from app.rag_pipeline import generate_response


# =========================================================
# FASTAPI INIT
# =========================================================

app = FastAPI(
    title="Agent Assist Copilot API"
)


# =========================================================
# REQUEST MODEL
# =========================================================

class ChatRequest(BaseModel):
    message: str


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/")
def health_check():

    return {
        "status": "running"
    }


# =========================================================
# CHAT ENDPOINT
# =========================================================

@app.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(
        request.message
    )

    return {
        "response": response
    }