from re import I
from turtle import pos, title
from typing import Optional
from fastapi import  FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int]

my_posts = [{"title":"title of post 1", "content":"content of post 1" , "id":1},
{"title":"title of post 2", "content":"content of post 2" , "id":2},{"title":"title of post 3", "content":"content of post 3" , "id":3}]

def find_post(id):
    for i in my_posts:
        if i["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/get/posts")
def get_posts():
    return {'post': my_posts}

@app.post("/create/post")
def create_post(post: Post):
    post_disc = post.dict()
    post_disc['id'] = randrange(0,100000)
    my_posts.append(post_disc)
    return {'post': post_disc}


@app.get("/get/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_details": post}


@app.get("/get/latest/post")
def get_latestpost():
    post = my_posts[len(my_posts)-1]
    return {"latest_post": post}