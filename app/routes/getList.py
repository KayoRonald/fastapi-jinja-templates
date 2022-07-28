from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.recipe_data import RECIPES

router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@router.get('/', status_code=200)
def root(request: Request) -> dict:

   return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "recipes": RECIPES},
    )