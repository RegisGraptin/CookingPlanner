
import os
import pytest

from cookingplanner.recipe.recipe_storage import RecipeStorage

RESSOURCE_FOLDER = os.path.join(os.path.dirname(__file__), "../ressources/")

TEST_CONFIG_PATH = "/tmp/"

@pytest.fixture
def fixture_recipe_storage():
    """Initiliaze the recipe storage for testing.

    Yields:
        RecipeStorage: Recipe storage instance for testing.
    """
    # Initiliaze the recipe storage
    _recipe_storage = RecipeStorage(TEST_CONFIG_PATH)
    yield _recipe_storage
    
    # Delete it 
    config_path = _recipe_storage.get_config_path()
    if os.path.exists(config_path):
        os.remove(config_path)
        
    _recipe_storage.destroy()


@pytest.fixture
def fixture_recipe_storage_with_data() -> RecipeStorage:
    """Load a recipe storage with data.

    Yields:
        RecipeStorage: Recipe storage with recipes on it.
    """
    _recipe_storage = RecipeStorage(RESSOURCE_FOLDER)
    yield _recipe_storage
    _recipe_storage.destroy()
    