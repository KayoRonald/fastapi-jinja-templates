from fastapi import FastAPI
from app.routes import getList

app = FastAPI()


app.include_router(getList.router)