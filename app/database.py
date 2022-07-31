from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:kjhyym415*@localhost:5432/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABSE_USERNAME}:{settings.DATABSE_PASSWORD}@{settings.DATABSE_HOSTNAME}:{settings.DATABSE_PORT}/{settings.DATABSE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = Session_local()
    try:
        yield db
        print("db connection success")
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='kjhyym415*', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
#     "title": "favorite foods", "content": "I like pizza", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
