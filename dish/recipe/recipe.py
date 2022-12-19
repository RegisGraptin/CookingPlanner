
import serpy

class RecipeStep:
    # {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
    
    def __init__(self, recipe_step: dict):
        self.type = recipe_step.get("@type", "")
        self.text = recipe_step.get("text", "")


class RecipeStepSerializer(serpy.Serializer):
    type = serpy.StrField(label="@type")
    text = serpy.StrField()


class Recipe(serpy.Serializer):
    
    def __init__(self, recipe_data: dict):
        self.name        = recipe_data.get("name", None)
        self.duration    = recipe_data.get("duration", None)
        self.prepTime    = recipe_data.get("prepTime", None)
        self.cookTime    = recipe_data.get("cookTime", None)
        self.totalTime   = recipe_data.get("totalTime", None)
        self.recipeYield = recipe_data.get("recipeYield", None)
        
        self.recipeIngredient   = recipe_data.get("recipeIngredient", [])
        self.recipeInstructions = [RecipeStep(step) for step in recipe_data.get("recipeInstructions", [])]
        self.recipeCuisine      = recipe_data.get("recipeCuisine", None)
        
    