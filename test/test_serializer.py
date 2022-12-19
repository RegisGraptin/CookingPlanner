
import json

from dish.recipe.recipe import RecipeStepSerializer, RecipeStep


def test_recipe_step_serializer():
    """Test the serialization on the RecipeStep class."""
    
    step_raw_data = {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."}
    
    recipe_step    = RecipeStep(step_raw_data)    
    serialize_data = RecipeStepSerializer(recipe_step).data
    
    assert step_raw_data["@type"] == serialize_data["@type"]
    assert step_raw_data["text"] == serialize_data["text"]
    assert step_raw_data == serialize_data


def test_recipe_serializer():
    pass
    


# def test_recipe_serializer():
    
#     recipe_raw_data = {"duration": "1 h 10 min", "name": "Boeuf Bourguignon rapide", "prepTime": "PT10M", "cookTime": "PT60M", "totalTime": "PT70M", "recipeYield": "6 personnes", "recipeIngredient": ["100 g de lardons", "50 g de beurre ou 3 cuill\u00e8res \u00e0 soupe d'huile", "2/3 l de vin rouge", "2 oignons", "1 gousse d'ail", "2 c.\u00e0.s de farine", "1 bouquet garni", "250 g de champignon de Paris (en bo\u00eete)", "sel", "poivre", "800 g de boeuf pour bourguignon"], "recipeInstructions": [{"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."}, {"@type": "HowToStep", "text": "Dans une cocotte minute, faire roussir la viande et les lardons dans l\u2019huile ou le beurre. "}, {"@type": "HowToStep", "text": "Ajouter les oignons, les champignons \u00e9goutt\u00e9s et saupoudrer de fariner. M\u00e9langer et laisser dorer un instant."}, {"@type": "HowToStep", "text": "Mouiller avec le vin rouge qui doit recouvrir la viande. "}, {"@type": "HowToStep", "text": "Saler et poivrer. "}, {"@type": "HowToStep", "text": "Ajouter l\u2019ail et le bouquet garni. "}, {"@type": "HowToStep", "text": "Fermer la cocotte minute. "}, {"@type": "HowToStep", "text": "Laisser cuire doucement 60 min \u00e0 partir de la mise en rotation de la soupape."}], "recipeCuisine": "Plat principal"}
    
#     recipe = Recipe(recipe_raw_data)

#     e = json.JSONEncoder()
#     print(e.encode(recipe))
    
#     # with open("/tmp/testing", "w") as f:
#     #     json.dump(recipe, f)
    
#     # print(recipe)
    
#     # recipe_encode = json(recipe)
    
#     # print(recipe_encode)
    
    