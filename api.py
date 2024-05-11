from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get('/hello')
async def hello():
    return {'msg': 'hei,hello!'}

class Person(BaseModel):
    name: str
    desc: str
    age: int
    year: int

@app.post("/item/")
async def create_item(person: Person):
    return person

@app.get("/items/{card_id}/{name}")
async def read_item(card_id: str, name:Optional[str] = None):
    return {"card_id": card_id,"name":name,"msg": "sf_token"}

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", reload=True)
