# from fastapi import FastAPI
# from fastapi.params import Body

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/createposts")
# def get_posts():
#     return {"data": "This is your posts"}

# # @app.post("/createposts")
# # def create_posts():
# #     return {"message": "Succesfully created posts"}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     return {"new_post": f"title: {payload["title"]}, content: {payload["content"]}"}

# SCHEMA USE PYDANTIC
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/createposts")
# def get_posts():
#     return {"data": "This is your posts"}

# @app.post("/createposts")
# def create_posts(post: Post):
#     print(post)
#     print(post.dict())
#     return {"data": post}

# STORING POSTS IN ARRAY/LIST
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_post}

# @app.post("/posts")
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_post.append(post_dict)
#     return {"data": post_dict}

# RETREIVE 1 POSTS
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# def find_posts(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts")
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_posts(id)
#     return {"post_detail": post}

# PATH SCOPE
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# def find_posts(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts")
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_posts(id)
#     return {"post_detail": post}

# CHANGE RESPONSE STATUS CODE
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# def find_posts(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_posts(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id: {id} was not found"}
#     return {"post_detail": post}

# DELETING POSTS
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# def find_posts(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_posts(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id: {id} was not found"}
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # find index in the array ID
#     index = find_index_post(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE POST
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food", "content": "I Like Pizza", "id": 2}]

# def find_posts(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_posts(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id: {id} was not found"}
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # find index in the array ID
#     index = find_index_post(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     post_dict = post.dict()
#     post_dict["id"] = id
#     my_posts[index] = post_dict
#     return {"data": post_dict}

# PYTHON POSTGRESQL CONNECTION WITH PSYCOPG2
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor

# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi_course', user='postgres', password='hadi2906', cursor_factory=RealDictCursor)
#     cur = conn.cursor()
#     print("Database connection was successfull!!")
# except Exception as error:
#     print("Conneting to database failed!")
#     print(f"Error: {error}")

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     # RETREIVING DATA
#     cur.execute("SELECT * FROM posts")
#     posts = cur.fetchall()
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # INSERT DATA
#     cur.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)", (post.title, post.content, post.published))
#     conn.commit()
#     return {"message": "Success"}

# @app.get("/posts/latest")
# def get_latest_post():
#     # post = my_posts[len(my_posts)-1]
#     # return {"detail": post}
#     return {"data": "Latest Post"}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cur.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
#     post = cur.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
#     deleted_post = cur.fetchone()
#     if not deleted_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     conn.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cur.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
#     updated_post = cur.fetchone()
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     conn.commit()
#     return {"data": updated_post}

# PYTHON CONNECTION DATABASE WITH SQLALCHEMY
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
# from . import models
# from .database import engine, SessionLocal, get_db

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def test_db(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}

# @app.get("/posts")
# def get_posts(db: Session = Depends(get_db)):
#     # RETREIVING DATA
#     posts = db.query(models.Post).all()
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post, db: Session = Depends(get_db)):
#     # INSERT DATA
#     # new_post = models.Post.created_posts(post)
#     # db.add(new_post)
#     new_posts = models.Post(**post.dict())
#     db.add(new_posts)
#     db.commit()
#     db.refresh(new_posts) # Give Back Data Like RETURNING
#     return {"message": new_posts}

# @app.get("/posts/latest")
# def get_latest_post(db: Session = Depends(get_db)):
#     # post = my_posts[len(my_posts)-1]
#     # return {"detail": post}
#     post = db.query(models.Post)
#     return {"data": "latest post"}

# @app.get("/posts/{id}")
# def get_post(id: int, db: Session = Depends(get_db)):
#     posts = db.query(models.Post).filter(models.Post.id == id).first()
#     if not posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"post_detail": posts}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     deleted_post = db.query(models.Post).filter(models.Post.id == id)
#     if not deleted_post.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     deleted_post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post, db: Session = Depends(get_db)):
#     posts_query = db.query(models.Post).filter(models.Post.id == id)

#     updated_post = posts_query.first()

#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")

#     posts_query.update(post.dict(), synchronize_session=False)
#     db.commit()
#     return {"data": posts_query.first(),
#             "message": "successfull"}

# RESPONSE MODEL
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from typing import Optional, List
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
# from . import models, schemas
# from .database import engine, SessionLocal, get_db
# from .utils import hash

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/posts", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # RETREIVING DATA
#     posts = db.query(models.Post).all()
#     return posts

# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     new_posts = models.Post(**post.dict())
#     db.add(new_posts)
#     db.commit()
#     db.refresh(new_posts)
#     return new_posts

# @app.get("/posts/latest")
# def get_latest_post(db: Session = Depends(get_db)):
#     # post = my_posts[len(my_posts)-1]
#     # return {"detail": post}
#     post = db.query(models.Post)
#     return {"data": "latest post"}

# @app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     posts = db.query(models.Post).filter(models.Post.id == id).first()
#     if not posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return posts

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     deleted_post = db.query(models.Post).filter(models.Post.id == id)
#     if not deleted_post.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")
#     deleted_post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db)):
#     posts_query = db.query(models.Post).filter(models.Post.id == id)

#     updated_post = posts_query.first()

#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists")

#     posts_query.update(post.dict(), synchronize_session=False)
#     db.commit()
#     return posts_query.first()

# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     hashed_password = hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/users/{id}", response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")

#     return user

# ROUTES
# from fastapi import FastAPI
# from . import models
# from .database import engine
# from .routes import post, user, auth, vote
# from .config import settings

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)
# app.include_router(vote.router)


# @app.get("/")
# def root():
#     return {"message": "Hello World"}


# ALEMBIC
from fastapi import FastAPI
from . import models
from .database import engine
from .routes import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
