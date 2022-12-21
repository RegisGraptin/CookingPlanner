
from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.recipe.recipe import Recipe, RecipeStep

TEST_CONFIG_PATH = "/tmp/"

def test_recipe_storage_initialization():
    recipe_storage = RecipeStorage(TEST_CONFIG_PATH)
    
    assert isinstance(recipe_storage, RecipeStorage)
    assert recipe_storage.get() == []
    
def tets_recipe_definition_from_raw_data():
    
    recipe_raw_data = {"duration": "1 h 10 min", "name": "Boeuf Bourguignon rapide", "prepTime": "PT10M", "cookTime": "PT60M", "totalTime": "PT70M", "recipeYield": "6 personnes", "recipeIngredient": ["100 g de lardons", "50 g de beurre ou 3 cuill\u00e8res \u00e0 soupe d'huile", "2/3 l de vin rouge", "2 oignons", "1 gousse d'ail", "2 c.\u00e0.s de farine", "1 bouquet garni", "250 g de champignon de Paris (en bo\u00eete)", "sel", "poivre", "800 g de boeuf pour bourguignon"], "recipeInstructions": [{"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."}, {"@type": "HowToStep", "text": "Dans une cocotte minute, faire roussir la viande et les lardons dans l\u2019huile ou le beurre. "}, {"@type": "HowToStep", "text": "Ajouter les oignons, les champignons \u00e9goutt\u00e9s et saupoudrer de fariner. M\u00e9langer et laisser dorer un instant."}, {"@type": "HowToStep", "text": "Mouiller avec le vin rouge qui doit recouvrir la viande. "}, {"@type": "HowToStep", "text": "Saler et poivrer. "}, {"@type": "HowToStep", "text": "Ajouter l\u2019ail et le bouquet garni. "}, {"@type": "HowToStep", "text": "Fermer la cocotte minute. "}, {"@type": "HowToStep", "text": "Laisser cuire doucement 60 min \u00e0 partir de la mise en rotation de la soupape."}], "recipeCuisine": "Plat principal"}
    
    recipe = Recipe(recipe_raw_data)
    
    assert recipe.name        == "Boeuf Bourguignon rapide"
    assert recipe.duration    == "1 h 10 min"
    assert recipe.prepTime    == "PT10M"
    assert recipe.cookTime    == "PT60M"
    assert recipe.totalTime   == "PT70M"
    assert recipe.recipeYield == "6 personnes"
    
    assert len(recipe.recipeIngredient)   == 9
    assert len(recipe.recipeInstructions) == 8
    
    assert recipe.recipeCuisine == "Plat principal"
    
    # Check the ingredient lists
    for ingredient in recipe.recipeIngredient:
        assert type(ingredient) == str
        
    assert recipe.recipeIngredient[0]  == "100 g de lardons"
    assert recipe.recipeIngredient[-1] == "800 g de boeuf pour bourguignon"
    
    # Check the recipe instruction
    for instruction in recipe.recipeInstructions:
        assert type(instruction) == type(RecipeStep)
        
    assert recipe.recipeInstructions[0].type == "HowToStep"
    assert recipe.recipeInstructions[0].text == "Hacher les oignons. Peler l'ail."
    
    assert recipe.recipeInstructions[-1].type == "HowToStep"
    assert recipe.recipeInstructions[-1].text == "Laisser cuire doucement 60 min à partir de la mise en rotation de la soupape."