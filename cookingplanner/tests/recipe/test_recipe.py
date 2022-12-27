
from cookingplanner.recipe.recipe import Recipe, RecipeStep

def test_recipe_definition_from_raw_data(fixture_raw_recipe):
    """TODO
    """
    
    recipe = Recipe(fixture_raw_recipe)
    
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
