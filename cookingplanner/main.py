from datetime import date

from cookingplanner.generator.dish_generator import DishWeeklyGenerator
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scraping_url import ScrapingURL
from cookingplanner.scraping.scraping_recipe import ScrapingRecipe
from cookingplanner.generator.week_generator import RegularWeekGenerator

SHOW_DATA = True


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


def show_url_recipe():
    """TODO
    """
    recipe_storage = RecipeStorage(config_path="./")
    recipes = recipe_storage.get()
    print("Number of recipes:", len(recipes))
    for recipe in recipes:
        print(recipe[0])


def generate_a_week():
    """TODO
    """

    # Initialize the recipe storage
    RecipeStorage(config_path="./")

    week_generator = RegularWeekGenerator()

    # weekGenerator = WeekGenerator(when)
    week = week_generator.generate(date.today())

    dishweek_generator = DishWeeklyGenerator()
    week = dishweek_generator.generator(week)

    print(week)


if __name__ == "__main__":

    generate_a_week()
