from fastapi import FastAPI

from app.api import api
from app.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api)


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}