from fastapi import FastAPI
from app.routes import getList, getById, deleteItem

app = FastAPI()


app.include_router(getList.router)
app.include_router(getById.router)
app.include_router(deleteItem.router)