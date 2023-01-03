import json
import os
import pytest

from cookingplanner.recipe.recipe import Recipe

RESSOURCE_FOLDER = os.path.join(os.path.dirname(__file__), "../ressources/")

@pytest.fixture
def fixture_test_recipe() -> Recipe:
    """Create a Recipe object for testing purpose.

    Returns:
        Recipe: Recipe object for testing.
    """
    return Recipe({}, "http://test.com")

@pytest.fixture
def fixture_raw_recipe() -> dict:
    """Load raw recipe data.

    Returns:
        dict: Raw recipe data 
    """
    # Get the filename 
    filepath = os.path.join(RESSOURCE_FOLDER, "boeuf_recipe.json")
    
    # Load the data
    with open(filepath, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data
