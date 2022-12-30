

import json
from cookingplanner.recipe.recipe_step import RecipeStep

class Recipe:
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
        
        if source is not None and source != "":
            self.source = source
        else:
            self.source = recipe_data.get("source", "")
         
        self.recipe_instructions = []
        for step_data in recipe_data.get("recipeInstructions", []):
            self.recipe_instructions.append(
                RecipeStep(step_data.get('type'), step_data.get('text'))
            )
            
    def get_recipe_name(self) -> str:
        """Get the recipe name.

        Returns:
            str: Recipe's name.
        """
        return self.name
    
    def to_json(self) -> str:
        """Encode object to json.

        Returns:
            str: Encoded object.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
