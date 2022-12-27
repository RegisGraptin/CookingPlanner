

import serpy


class RecipeStep:
    """Recipe Step class.
    
    Define a step in the recipe.
    Example: 
        {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
        
    TODO :: Improvment by decode it before hand. Instead of decoded it here.
    """
    
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
