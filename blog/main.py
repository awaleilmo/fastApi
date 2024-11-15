from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blogs(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create_blog(request: Blogs):
    return {'data': {'title': request.title, 'body': request.body}}