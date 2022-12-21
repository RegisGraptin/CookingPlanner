from datetime import date

from cookingplanner.generator.dishGenerator import DishWeeklyGenerator
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scrapingurl import ScrapingURL
from cookingplanner.scraping.scrapingrecipe import ScrapingRecipe
from cookingplanner.generator.week import WeekGenerator, RegularWeekGenerator

SHOW_DATA = True

def generate_data():
    
    recipe_storage = RecipeStorage(config_path="./")
    
    # Get recipes url
    scrapingURL = ScrapingURL(n_pages=1)
    recipe_urls = scrapingURL.scrap()
    
    print("Load {0} recipes".format(len(recipe_urls)))
    
    scrapingRecipe = ScrapingRecipe()
    for recipe_url in recipe_urls:
        # Extract and add the recipe
        recipe = scrapingRecipe.scrap(recipe_url)
        recipe_storage.add(recipe_url, recipe)
    
    print("Extract and saved all recipes")

def show_url_recipe():
    recipe_storage = RecipeStorage(config_path="./")
    recipes = recipe_storage.get()
    print("Number of recipes:", len(recipes))
    for recipe in recipes:
        print(recipe[0])
    

def generate_a_week():
    
    # Initialize the recipe storage
    RecipeStorage(config_path="./")
    
    weekGenerator = RegularWeekGenerator()
    
    # weekGenerator = WeekGenerator(when)
    week = weekGenerator.generate(date.today())
    
    dishweekgenerator = DishWeeklyGenerator()
    week = dishweekgenerator.generator(week)
    
    print(week)


if __name__ == "__main__":
    
    generate_a_week()
