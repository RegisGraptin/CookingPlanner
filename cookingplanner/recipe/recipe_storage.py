import os
import json
import random
from typing import List, Tuple
from cookingplanner.recipe.recipe import Recipe

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
            for url, recipe in self.get_all_recipes_with_url():
                recipe_data.append((url, recipe.to_json()))
            
            data["recipes"] = recipe_data
            
            json.dump(data, file)
    
    def read(self):
        """Read the data from the json file."""
        with open(self.config_path, 'r', encoding="utf-8") as file:
            self.data = json.load(file)
            
        for index in range(len(self.data['recipes'])):
            self.data['recipes'][index][1] = Recipe(json.loads(self.data['recipes'][index][1]))
        
        
        
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
        
        self.data['recipes'].append(
            (url, recipe)
        )
        self.save()
        
    def get_all_recipes_with_url(self) -> List[Tuple[str, Recipe]]:
        """Get all recipes from our recipe storage.

        Returns:
            List[Recipe]: List of all the recipe.
        """
        return self.data.get('recipes', [])
        
    def get(self, url: str) -> Recipe:
        """Given an url, get the saved recipe.

        Args:
            url (str): Requested url recipe.

        Returns:
            Recipe: Recipe associated to the requested url.
        """
        for tup in self.get_all_recipes_with_url():
            if tup[0] == url:
                return tup[1]
        return None
    
    def exists(self, url: str) -> bool:
        """Indicate if the given url already exists.

        Args:
            url (str): Url we want to check

        Returns:
            bool: True if the url is already presents.
        """
        return any(url == tup[0] for tup in self.get_all_recipes_with_url())
    
    def get_config_path(self) -> str:
        """Get the configuration file path.

        Returns:
            str: Path of the configuration file.
        """    
        return self.config_path


    @classmethod
    def destroy(cls):
        """Destroy the current object.
        
        Use for testing purpose. Do not use in production.
        """
        del cls._instances[cls]
