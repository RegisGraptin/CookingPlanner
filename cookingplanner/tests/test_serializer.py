
import json

from cookingplanner.recipe.recipe import Recipe
from cookingplanner.recipe.recipe_step import RecipeStep


def test_recipe_step_serializer():
    """Test the serialization on the RecipeStep class."""
    
    step_raw_data = {"type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."}
    
    recipe_step    = RecipeStep(step_raw_data.get('type'), step_raw_data.get('text'))
    serialize_data = json.loads(recipe_step.to_json())
    
    assert step_raw_data["type"] == serialize_data["type"]
    assert step_raw_data["text"] == serialize_data["text"]
    assert step_raw_data == serialize_data


def test_recipe_serializer(fixture_raw_recipe):
    """Test the serialization on the Recipe class."""

    recipe            = Recipe(fixture_raw_recipe)
    serialized_recipe = json.loads(recipe.to_json())
    
    assert serialized_recipe['source'] is not None
    assert serialized_recipe['recipe_ingredient'] is not None
    assert serialized_recipe['recipe_instructions'] is not None
    
    assert len(serialized_recipe['recipe_ingredient']) > 0
    assert len(serialized_recipe['recipe_ingredient']) > 0
    
    assert serialized_recipe['recipe_ingredient'][0] == "100 g de lardons"
    assert serialized_recipe['recipe_ingredient'][-1] == "800 g de boeuf pour bourguignon"
    
    assert serialized_recipe['recipe_instructions'][0]['type'] == "HowToStep"
    assert serialized_recipe['recipe_instructions'][0]['text'] == "Hacher les oignons. Peler l'ail."
    
    assert serialized_recipe['recipe_instructions'][-1]['type'] == "HowToStep"
    assert serialized_recipe['recipe_instructions'][-1]['text'] == "Laisser cuire doucement 60 min à partir de la mise en rotation de la soupape."
