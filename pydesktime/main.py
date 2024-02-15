from fastapi import FastAPI
from dataclasses import dataclass
from pydantic import BaseModel

# from typing import Optional
# from typing import Union

class Post(BaseModel):
    title: str
    message: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/create_post")
def create_posts(new_post: Post):
    print(new_post)
    return {"data":"New Post"}