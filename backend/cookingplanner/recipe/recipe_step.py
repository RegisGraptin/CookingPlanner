
import json


class RecipeStep:
    """Recipe Step class.
    
    Define a step in the recipe.
    Example: 
        {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
        
        {"type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
        
    TODO :: Improvment by decode it before hand. Instead of decoded it here.
    """
    
    def __init__(self, step_type: str, step_text: str):
        self.type = step_type
        self.text = step_text


    def to_json(self) -> str:
        """Convert current object to json format.

        Returns:
            str: Json encoding.
        """
        return json.dumps(self, default=lambda o: o.__dict__,  sort_keys=True, indent=4)
