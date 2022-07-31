from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy.orm import Session

# Dependency


app = FastAPI()

my_post = [{"id": 1, "title": "title1", "content": "content1"},
           {"id": 2, "title": "title2", "content": "content2"}]


class Post(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False
    # rating: Optional[int] = None


while 1:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database='fastapi',
            user="postgres",
            password="kjhyym415*",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database Connection Success")
        break
    except Exception as error:
        print("Connecting Fail")
        print("error: ", error)
        time.sleep(5)


@app.get("/")
async def root():
    return {"data": my_post}


@app.get("/posts")
def get_post():
    cursor.execute(""" SELECT * FROM products """)
    posts = cursor.fetchall()
    print(posts)
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute(
        f"""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
        (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(
        """ SELECT * FROM posts  WHERE id = %s""", (str(id))
    )
    get_post = cursor.fetchone()
    return {"data": get_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING * """, (str(id))
    )
    delet_post = cursor.fetchone()
    conn.commit()

    if delet_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id{id} does not exist")
    return {"data": delet_post}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content =%s, published=%s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, id))
    update_post = cursor.fetchone()
    conn.commit()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    return {"data": update_post}
