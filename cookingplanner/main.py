from datetime import date

from cookingplanner.generator.dish_generator import DishWeeklyGenerator
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.generator.week_generator import RegularWeekGenerator

SHOW_DATA = True


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
