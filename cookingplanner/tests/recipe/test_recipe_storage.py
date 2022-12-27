
from cookingplanner.recipe.recipe import Recipe
from cookingplanner.recipe.recipe_storage import RecipeStorage


def test_recipe_storage_initialization(fixture_recipe_storage: RecipeStorage):
    """Initialize a recipe storage.

    Args:
        fixture_recipe_storage (RecipeStorage): Recipe storage for testing.
    """
    assert isinstance(fixture_recipe_storage, RecipeStorage)
    assert fixture_recipe_storage.get_all_recipes_with_url() == []

def test_recipe_storage_add_recipe(
    fixture_recipe_storage: RecipeStorage, 
    fixture_test_recipe: Recipe):
    """Test the adding function of the recipe storage.

    Args:
        recipe_storage (RecipeStorage): Recipe storage for testing.
        test_recipe (Recipe): Test recipe.
    """
    # Add a new recipe
    fixture_recipe_storage.add(fixture_test_recipe.source, fixture_test_recipe)
    assert fixture_recipe_storage.exists(fixture_test_recipe.source)
    
    # Get the recipe saved 
    recipe = fixture_recipe_storage.get(fixture_test_recipe.source)
    assert recipe == fixture_test_recipe
