from fastapi import FastAPI
import random
from pydantic import BaseModel, Field
app = FastAPI()


@app.get("/random_numbers")
def get_random_numbers():
    random_numbers = [random.randint(1, 1000) for _ in range(5)]
    return random_numbers

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    item = {"item_id": item_id, "name": "Item Name"}
    return item

@app.get("/items")
def get_items(query_param1: int, query_param2: str):
    items = {"query_param1": query_param1, "query_param2": query_param2}
    return items

@app.get("/items/{item_id}/info")
def get_item_info(item_id: str, query_param1: int, query_param2: int):
    item_info = {"item_id": item_id, "query_param1": query_param1, "query_param2": query_param2}
    return item_info


class Actors(BaseModel):
    actor_id: int
    name: str
    surname: str
    age: int
    sex: str

@app.post("/actor")
def create_actor(actors: Actors):
    return actors

class Actor(BaseModel):
    actor_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=20)
    surname: str = Field(..., min_length=2, max_length=20)
    age: int = Field(..., ge=0, le=100)
    sex: str = Field(..., pattter='^(male|female)$')

@app.post("/actors")
def create_actor(actor: Actor):
    return actor