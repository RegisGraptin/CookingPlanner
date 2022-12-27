import argparse
from datetime import date

from cookingplanner.generator.meal_generator import UniqueMealStrategy
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.generator.week_generator import WorkWeekGenerator
from cookingplanner.scraping.scraping import Scraping
from cookingplanner.scraping.scraping_url import ScrapingURL

SHOW_DATA = True

recipe_storage = RecipeStorage(config_path="./")

def generate_data(n_pages : int = 10):
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


def generate_next_week(strategy: str):
    """TODO
    """
    today = date.today()

    # Generate the template for the next week
    working_week = WorkWeekGenerator().generate(today)

    print(strategy)

    if strategy == "unique":

        meal_generator = UniqueMealStrategy()
        working_week = meal_generator.generate(working_week)

        print(working_week)

    else:
        print(f"The strategy {strategy} does not exist!")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog = 'Cooking Planner',
    )
    
    parser.add_argument('--update', action="store_true")
    parser.add_argument('strategy', action="store", type=str)
    args = parser.parse_args()
    
    if args.update:
        generate_data()
        
    if args.strategy:
        generate_next_week(args.strategy)
    