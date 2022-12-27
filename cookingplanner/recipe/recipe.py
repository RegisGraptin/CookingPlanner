
import serpy
from cookingplanner.recipe.recipe_step import RecipeStep, RecipeStepSerializer

class Recipe(): # serpy.Serializer
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
        
        self.recipe_cuisine      = recipe_data.get("recipeCuisine", None)
        
        self.source = source
         
        self.recipe_instructions = []
        for step_data in recipe_data.get("recipeInstructions", []):
            self.recipe_instructions.append(
                RecipeStep(step_data.get('type'), step_data.get('text'))
            )
        
    

class RecipeSerializer(serpy.Serializer):
    """Recipe Serializer class."""
    
    name         = serpy.StrField()
    duration     = serpy.StrField()
    prep_time    = serpy.StrField()
    cook_time    = serpy.StrField()
    total_time   = serpy.StrField()
    recipe_yield = serpy.StrField()
    
    recipe_ingredient = serpy.Serializer(serpy.StrField, many=True)
    recipe_instructions = serpy.Serializer(RecipeStepSerializer, many=True)
    
    recipe_cuisine = serpy.StrField()
    source = serpy.StrField()
