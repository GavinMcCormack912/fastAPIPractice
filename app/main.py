from fastapi import FastAPI
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import post, user, auth, vote

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},{"title": "title of post 2", "content": "content of post 2", "id": 2}]



# """ HELPER FUNCTIONS """
# def find_post(id) :
#     for p in my_posts:
#         if p['id'] == (id):
#             return p
        
# def find_post_index(id):
#     postID:int = -1
#     print(id)
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             postID = i
#     return postID

""" CRUD REQUESTS"""

# @app.get("/")
# def root():
#     return {"message": "Hello World!"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     return {"status": "success"}

#ORM VERSION

# @app.get("/posts", response_model=List[schemas.Post])
# def test_posts(db: Session = Depends(get_db)):

#     posts = db.query(models.Post).all()
#     return posts


# # RAW SQL VERSION
# # @app.get("/posts")
# # def get_posts():
# #     cursor.execute(""" SELECT * FROM posts """)
# #     posts = cursor.fetchall()
# #     print(posts)
# #     return {"data": posts}


# @app.post("/createpost", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def make_post(post: schemas.PostBase, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *; """, 
#     #             (post.title, post.content, post.published)
#     # )
#     # new_post = cursor.fetchone()
#     # conn.commit()
#     #print(post.dict())
#     new_post = models.Post(**post.dict()) #unpack the dictionary for sqlalchemy!
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post
# #force a user to send in a specific structure with an http request by using BaseModel from pydantic


# #{id} on the next get http request could be "latest", so this MUST come first
# @app.get("/posts/latest")
# def get_latest_post(db: Session = Depends(get_db)):
#     cursor.execute(""" SELECT * FROM posts ORDER BY created_at DESC LIMIT 1 """, (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     return post


# @app.get("/posts/{id}")  #path parameter to the id of the post a user wants to see
# def get_post(id:int, db: Session = Depends(get_db)):
#     # cursor.execute(""" SELECT * FROM posts WHERE id = (%s) """, (str(id),))
#     # post = cursor.fetchone()
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     return post

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int, db: Session = Depends(get_db)):
#     #deleting post
#     #find the index in the array w/ requried ID
#     # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
#     # post = cursor.fetchone()
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if not post.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
    

# @app.put("/posts/{id}")
# def update_post(id:int, post: schemas.PostBase, db: Session = Depends(get_db)):
#     # cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""", 
#     #                (post.title, post.content. post.published, str(id))
#     # )
#     # updated_post = cursor.fetchone()
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     updated_post = post_query.first()
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
   
#     #conn.commit()
#     post_query.update(post.dict(), synchronize_session=False)
#     db.commit()
#     return post_query.first()


# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password before saving it to the db. user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password;
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user;


# @app.get("/users/{id}", response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first();

#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

#     return user