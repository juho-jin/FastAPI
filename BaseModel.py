# Python 3.6 and above => This Python version 3.9.13
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : Union[str, None] = None
    price : float
    tax : Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item:Item):
    return item