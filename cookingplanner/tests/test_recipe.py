
import os
import pytest
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.recipe.recipe import Recipe, RecipeStep

TEST_CONFIG_PATH = "/tmp/"

@pytest.fixture(name="recipe_storage")
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

@pytest.fixture(name="test_recipe")
def fixture_test_recipe() -> Recipe:
    """Create a Recipe object for testing purpose.

    Returns:
        Recipe: Recipe object for testing.
    """
    return Recipe({}, "http://test.com")

def test_recipe_storage_initialization(recipe_storage):
    """Initialize a recipe storage."""
    assert isinstance(recipe_storage, RecipeStorage)
    assert recipe_storage.get_all_recipes_with_url() == []

def test_recipe_storage_add_recipe(recipe_storage: RecipeStorage, test_recipe: Recipe):
    """Test the adding function of the recipe storage.

    Args:
        recipe_storage (RecipeStorage): Recipe storage for testing.
        test_recipe (Recipe): Test recipe.
    """
    # Add a new recipe
    recipe_storage.add(test_recipe.source, test_recipe)
    assert recipe_storage.exists(test_recipe.source)
    
    # Get the recipe saved 
    recipe = recipe_storage.get(test_recipe.source)
    assert recipe == test_recipe
    
    
def test_recipe_definition_from_raw_data():
    """TODO
    """
    
    recipe_raw_data = {"duration": "1 h 10 min", "name": "Boeuf Bourguignon rapide", "prepTime": "PT10M", "cookTime": "PT60M", "totalTime": "PT70M", "recipeYield": "6 personnes", "recipeIngredient": ["100 g de lardons", "50 g de beurre ou 3 cuill\u00e8res \u00e0 soupe d'huile", "2/3 l de vin rouge", "2 oignons", "1 gousse d'ail", "2 c.\u00e0.s de farine", "1 bouquet garni", "250 g de champignon de Paris (en bo\u00eete)", "sel", "poivre", "800 g de boeuf pour bourguignon"], "recipeInstructions": [{"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."}, {"@type": "HowToStep", "text": "Dans une cocotte minute, faire roussir la viande et les lardons dans l\u2019huile ou le beurre. "}, {"@type": "HowToStep", "text": "Ajouter les oignons, les champignons \u00e9goutt\u00e9s et saupoudrer de fariner. M\u00e9langer et laisser dorer un instant."}, {"@type": "HowToStep", "text": "Mouiller avec le vin rouge qui doit recouvrir la viande. "}, {"@type": "HowToStep", "text": "Saler et poivrer. "}, {"@type": "HowToStep", "text": "Ajouter l\u2019ail et le bouquet garni. "}, {"@type": "HowToStep", "text": "Fermer la cocotte minute. "}, {"@type": "HowToStep", "text": "Laisser cuire doucement 60 min \u00e0 partir de la mise en rotation de la soupape."}], "recipeCuisine": "Plat principal"}
    
    recipe = Recipe(recipe_raw_data)
    
    assert recipe.name        == "Boeuf Bourguignon rapide"
    assert recipe.duration    == "1 h 10 min"
    assert recipe.prep_time    == "PT10M"
    assert recipe.cook_time    == "PT60M"
    assert recipe.total_time   == "PT70M"
    assert recipe.recipe_yield == "6 personnes"
    
    assert len(recipe.recipe_ingredient)   == 11
    assert len(recipe.recipe_instructions) == 8
    
    assert recipe.recipe_cuisine == "Plat principal"
    
    # Check the ingredient lists
    for ingredient in recipe.recipe_ingredient:
        assert isinstance(ingredient, str)

    assert recipe.recipe_ingredient[0]  == "100 g de lardons"
    assert recipe.recipe_ingredient[-1] == "800 g de boeuf pour bourguignon"
    
    # Check the recipe instruction
    for instruction in recipe.recipe_instructions:
        assert isinstance(instruction, RecipeStep)
        
    assert recipe.recipe_instructions[0].type == "HowToStep"
    assert recipe.recipe_instructions[0].text == "Hacher les oignons. Peler l'ail."
    
    assert recipe.recipe_instructions[-1].type == "HowToStep"
    assert recipe.recipe_instructions[-1].text == "Laisser cuire doucement 60 min à partir de la mise en rotation de la soupape."
