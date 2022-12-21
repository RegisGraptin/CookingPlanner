
import random

from typing import List , Tuple

from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.generator.week_generator import Week

class UniqueRecipeStrategy:
    
    def __init__(self, recipes: List[Tuple[str, dict]]) -> None:
        """Unique Recipe Strategy

        Args:
            recipe_storage (Recipes): _description_
        """
        self.recipes = recipes
        
        self.recipes_seen = set()
        
    def reset(self):
        self.recipes_seen = set()
        
    def generate(self) -> str:
        """Return a recipe that the user never see.

        Returns:
            str: Recipe url
        """
        
        # Choose a random recipe
        chosen_recipe, _ = random.choice(self.recipes)
        
        print(len(self.recipes))
        # print(self.recipes)
        
        while chosen_recipe in self.recipes_seen:
            chosen_recipe, _ = random.choice(self.recipes)
        
        
        # Add it to the list of seen
        self.recipes_seen.add(chosen_recipe)
        
        return chosen_recipe
    


class DishWeeklyGenerator:
    
    def __init__(self) -> None:
        
        # Get the recipe possible
        self.recipe_storage = RecipeStorage()
        self.recipes = self.recipe_storage.get()
        
        self.strategy = UniqueRecipeStrategy(self.recipes)
        
    def generator(self, week: Week) -> Week:
        
        # Get the day of the weeks
        days = week.get_days()
        
        for day in days:
            dishes = day.get_dishes()
            for dish in dishes:
                moment = dish.get_moment()
                
                recipe = self.strategy.generate()
                
                dish.set_recipe(recipe)
        
        return week
            
        
    