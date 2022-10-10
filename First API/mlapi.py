# Basic Dependencies
from unittest import async_case
from fastapi import FastAPI

# App initialization
app = FastAPI()

@app.get('/')
async def index():
    return {'Msg':"Hello World!"}