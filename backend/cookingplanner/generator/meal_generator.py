
from abc import ABCMeta, abstractmethod
import random
from typing import List, Tuple

from cookingplanner.generator.meal import Day, Meal, Period
from cookingplanner.recipe.recipe import Recipe
from cookingplanner.recipe.recipe_storage import RecipeStorage

class PeriodMealGenerator(metaclass=ABCMeta):
    """TODO"""
        
    def generate(self, period: Period) -> Period:
        """Given a period, generate the meal for each day.

        Args:
            period (Period): Period where we want to generate meal

        Returns:
            Period: Period with the meals assign.
        """
        days = period.get_days()
        for day in days:
            
            # Get the unset meal
            meals = day.get_meals()
            for meal in meals:
                
                # Generate the meal
                self.generate_meal(day, meal)
                
        return period

    @abstractmethod
    def generate_meal(self, day: Day, meal: Meal):
        """Generate the meal for the given one.

        Args:
            day (Day): Day of the meal.
            moment (Meal): Meal we want to generate.
        """


class UniqueMealStrategy(PeriodMealGenerator):
    """Unique Meal Strategy class.
    
    Given a period, we generate meals by using a different recipe each time.

    Args:
        PeriodMealGenerator: Abstract class.
    """
    
    def __init__(self, 
                 recipe_storage: RecipeStorage = None) -> None:
        
        if recipe_storage is None:
            recipe_storage = RecipeStorage()
        
        self.recipes : List[Tuple[str, Recipe]]= recipe_storage.get_all_recipes_with_url()
        self.recipes_seen = set()
    
    
    def generate_meal(self, day: Day, meal: Meal):
        """Generate a unique meal given the day.

        Args:
            day (Day): Day of the generated meal.
            meal (Meal): Meal we want to generate.
        """
        
        # Choose a random recipe
        chosen_recipe_url, chosen_recipe = random.choice(self.recipes)
        
        while chosen_recipe_url in self.recipes_seen:
            chosen_recipe_url, chosen_recipe = random.choice(self.recipes)
        
        # Add it to the list of seen
        self.recipes_seen.add(chosen_recipe_url)
        
        # Set the recipe to the current meal
        meal.set_recipe(chosen_recipe)
        
    def reset(self):
        """TODO"""
        self.recipes_seen = set()
