from datetime import date

from cookingplanner.generator.dish_generator import DishWeeklyGenerator
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.generator.week_generator import RegularWeekGenerator
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


def generate_a_week():
    """TODO
    """

    week_generator = RegularWeekGenerator()

    # weekGenerator = WeekGenerator(when)
    week = week_generator.generate(date.today())

    dishweek_generator = DishWeeklyGenerator()
    week = dishweek_generator.generator(week)

    print(week)


if __name__ == "__main__":
    
    # TODO :: Add script call for the generation of data.
    
    generate_data()
