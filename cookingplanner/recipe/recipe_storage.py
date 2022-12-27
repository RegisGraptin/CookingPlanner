import os
import json
import random
from cookingplanner.recipe.recipe import RecipeSerializer

from cookingplanner.utils.singleton import SingletonMeta

class RecipeStorage(metaclass=SingletonMeta):
    """RecipeStorage class.
    
    Store all the recipe extracted online.
    The current architecture store the recipe in a list format.
    Each element is defined as a tuple. The first element is the source url
    where we extract the recipe. The second element is the Recipe.
    
    Args:
        metaclass (SingletonMeta, optional): Singleton class. Defaults to SingletonMeta.
    """
    
    CONFIG_NAME   = "recipes.json"
    CONFIG_FOLDER = "./"
    
    def __init__(self, config_path: str = CONFIG_FOLDER) -> None:
        self.config_path = os.path.join(config_path, RecipeStorage.CONFIG_NAME)
        
        self.data = {}
        self.data['recipes'] = []
        
        if os.path.exists(self.config_path):
            # Read the file
            self.read()
    
    def save(self):
        """Save the data"""
        
        data = {}
        recipe_data = []
        
        with open(self.config_path, 'w', encoding="utf-8") as file:
            for url, recipe in self.get():
                recipe_data.append((url, RecipeSerializer(recipe).data))
            
            data["recipes"] = recipe_data
            
            json.dump(data, file)
    
    def read(self):
        """Read the data from the json file."""
        with open(self.config_path, 'r', encoding="utf-8") as file:
            self.data = json.load(file)
            
    
    def get_random(self):
        """TODO

        Returns:
            _type_: _description_
        """
        return random.choice(self.data['recipes'])
    
    def add(self, url: str, recipe: dict):
        """Add the recipe and save it.

        Args:
            url (str): _description_
            recipe (_type_): _description_
        """
        
        # TODO: Verify if recipe exists or not
        if self.exists(url):
            return
        
        print("Here ?")
        
        self.data['recipes'].append(
            (url, recipe)
        )
        self.save()
        
    def get(self):
        """TODO

        Returns:
            _type_: _description_
        """
        return self.data.get('recipes', [])
    
    def exists(self, url: str) -> bool:
        """Indicate if the given url already exists.

        Args:
            url (str): Url we want to check

        Returns:
            bool: True if the url is already presents.
        """
        return any(url == tup[0] for tup in self.get())
    
    
    def get_config_path(self) -> str:
        """Get the configuration file path.

        Returns:
            str: Path of the configuration file.
        """
        
        return self.config_path
