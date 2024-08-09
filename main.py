from typing import Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_post = []

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_post}

@app.post("/createposts")
async def create_posts(data: Post):
    post_dump = data.model_dump()
    post_dump["id"] = randrange(0, 1000000)
    my_post.append(post_dump)
    return {
        "message": "Post has been created",
        "data": data
        }

@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = 404
    return {"data": find_post(id)}