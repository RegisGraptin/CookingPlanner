
# from marmiton.dish.recipe import Recipes

from dish.recipe.recipe_storage import RecipeStorage

TEST_CONFIG_PATH = "/tmp/"



def test_recipe():
    recipe_storage = RecipeStorage(TEST_CONFIG_PATH)
    
    assert isinstance(recipe_storage, RecipeStorage)
    assert recipe_storage.get() == []
    
    