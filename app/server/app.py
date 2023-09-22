from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.api.v1.endpoints.ask import router as AskRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(AskRouter, tags=["AI Visual Question Answering"], prefix="/ask")

@app.get("/")
def start_app():
    return {"Description":"ML APIs Using FastAPI"}