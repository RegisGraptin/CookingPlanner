import os
import json
import random

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
            with open(self.config_path, 'r', encoding="utf-8") as file:
                self.data = json.load(file)
    
    def save(self):
        """Save the data"""
        with open(self.config_path, 'w', encoding="utf-8") as file:
            json.dump(self.data, file)
                
    
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
        
        urls = [u[0] for u in self.data['recipes']]
        if url in urls: 
            return 
        
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
    