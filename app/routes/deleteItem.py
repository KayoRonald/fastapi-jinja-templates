from fastapi import APIRouter, HTTPException
from typing import Any
from app.recipe_data import RECIPES
from app.schema import Recipe
router = APIRouter()

@router.delete('/recipe/{id_recipe}', status_code=200, response_model= Recipe)
def delete_recipe(*, id_recipe: int) -> Any:
  """
    Excluir uma receita (somente na memória)
  """
  result = [recipe for recipe in RECIPES if recipe["id"] == id_recipe]
  if not result:
    raise HTTPException(
      status_code= 404,
      detail=f"Não encotramos o produto com esse id: {id_recipe}"
    )
  return RECIPES.pop(id_recipe -1)