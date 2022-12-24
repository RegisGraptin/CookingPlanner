

from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scraping_recipe import ScrapingRecipe
from cookingplanner.scraping.scraping_url import ScrapingURL


class ScrapingData():
    """TODO"""
    

def generate_data():
    """TODO
    """

    recipe_storage = RecipeStorage(config_path="./")

    # Get recipes url
    scraping_url = ScrapingURL(n_pages=1)
    recipe_urls = scraping_url.scrap()

    print(f"Load {len(recipe_urls)} recipes")

    scraping_recipe = ScrapingRecipe()
    for recipe_url in recipe_urls:
        # Extract and add the recipe
        recipe = scraping_recipe.scrap(recipe_url)
        recipe_storage.add(recipe_url, recipe)

    print("Extract and saved all recipes")
