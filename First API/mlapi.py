# Basic Dependencies
from unittest import async_case
from fastapi import FastAPI
from pydantic import BaseModel

# App initialization
app = FastAPI()

#@app.get('/')
#async def index():
#    return {'Msg':"Hello World!"}

class ScoringItem(BaseModel):
    YearsAtCompany:float
    EmployeeSatisfaction: float
    Position: str
    Salary: int



@app.post('/')
async def ScoringItem(item:ScoringItem):
    pass