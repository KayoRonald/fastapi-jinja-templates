from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.recipe_data import RECIPES
from app.schema import Recipe, RecipeSearchResults
router = APIRouter()

@router.get('/recipe/{id_recipe}', status_code=200, response_model= Recipe)
def fetch_recipe(*, id_recipe: int) -> dict:
  result = [recipe for recipe in RECIPES if recipe['id'] == id_recipe]
            
  if not result:
    raise HTTPException(
      status_code= 404,
      detail=f"Não encotramos o produto com esse id: {id_recipe}"
    )
  return result[0]
    
# Exemple: /search/?keyword=Chicken
@router.get('/search/', status_code=200, response_model= RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}