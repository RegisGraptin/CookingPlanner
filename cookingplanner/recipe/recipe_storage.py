import os
import json
import random

from cookingplanner.utils.singleton import SingletonMeta

class RecipeStorage(metaclass=SingletonMeta):
    """TODO

    Args:
        metaclass (_type_, optional): _description_. Defaults to SingletonMeta.

    Returns:
        _type_: _description_
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
    