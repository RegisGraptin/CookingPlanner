
from datetime import date

from fastapi import FastAPI, HTTPException, status

from cookingplanner.config import Config
from cookingplanner.generator.meal import Week
from cookingplanner.generator.meal_generator import UniqueMealStrategy
from cookingplanner.generator.week_generator import WorkWeekGenerator
from cookingplanner.models.database import Database
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scraping import Scraping
from cookingplanner.scraping.scraping_url import ScrapingURL

from cookingplanner.routers.auth import router as router_auth
from cookingplanner.routers.profile import router as router_profile


# Load the configuration, database and storage
config = Config()

database = Database()
database.generate()

recipe_storage = RecipeStorage(config_path="./")


app = FastAPI(openapi_url=config.get_openapi_url())

app.include_router(router_auth, prefix="/auth")
app.include_router(router_profile, prefix="/profile")

@app.get("/generate/{n_pages}", status_code=status.HTTP_201_CREATED)
def generate_data(n_pages: int = 10):
    """Given a strategy, we extract new recipe from it.

    Args:
        n_pages (int, optional): Number of page for search new urls recipe in our strategy. 
                                 Defaults to 10.
    """
    
    # Define our strategy
    scraping_url = ScrapingURL(n_pages = n_pages)
    
    # Scrap and save the new recipe
    scraping = Scraping(scraping_url=scraping_url)
    scraping.scrap()
    

def show_url_recipe():
    """TODO
    """
    recipes = recipe_storage.get()
    print("Number of recipes:", len(recipes))
    for recipe in recipes:
        print(recipe[0])


@app.get("/week/work/{strategy}", status_code=status.HTTP_201_CREATED)
def generate_next_week(strategy: str) -> Week:
    """TODO
    """
    today = date.today()

    # Generate the template for the next week
    working_week = WorkWeekGenerator().generate(today)

    if strategy == "unique":

        generated_meal_week = UniqueMealStrategy(recipe_storage).generate(working_week)
        return generated_meal_week

    raise HTTPException(status_code=404, detail=f"The strategy {strategy} does not exist!")
