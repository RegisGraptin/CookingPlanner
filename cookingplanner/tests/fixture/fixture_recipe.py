import pytest

from cookingplanner.recipe.recipe import Recipe

@pytest.fixture
def fixture_test_recipe() -> Recipe:
    """Create a Recipe object for testing purpose.

    Returns:
        Recipe: Recipe object for testing.
    """
    return Recipe({}, "http://test.com")
