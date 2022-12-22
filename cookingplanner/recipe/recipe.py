
import serpy

class RecipeStep:
    """TODO
    """
    # {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
    
    def __init__(self, recipe_step: dict):
        self.type = recipe_step.get("@type", "")
        self.text = recipe_step.get("text", "")


class RecipeStepSerializer(serpy.Serializer):
    """TODO

    Args:
        serpy (_type_): _description_
    """
    type = serpy.StrField(label="@type")
    text = serpy.StrField()


class Recipe(serpy.Serializer):
    """TODO

    Args:
        serpy (_type_): _description_
    """
    
    def __init__(self, recipe_data: dict, source: str = ""):
        self.name         = recipe_data.get("name", None)
        self.duration     = recipe_data.get("duration", None)
        self.prep_time    = recipe_data.get("prepTime", None)
        self.cook_time    = recipe_data.get("cookTime", None)
        self.total_time   = recipe_data.get("totalTime", None)
        self.recipe_yield = recipe_data.get("recipeYield", None)
        
        self.recipe_ingredient   = recipe_data.get("recipeIngredient", [])
        self.recipe_instructions = [RecipeStep(step) 
                                   for step in recipe_data.get("recipeInstructions", [])]
        self.recipe_cuisine      = recipe_data.get("recipeCuisine", None)
        
        self.source = source
    