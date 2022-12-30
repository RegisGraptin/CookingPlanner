
from abc import ABCMeta, abstractmethod
import random

from cookingplanner.generator.meal import Day, Meal, Moment, Period
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
            dishes = day.get_meals()
            for dish in dishes:
                moment = dish.get_moment()
                recipe = self.generate_meal(day, moment)
                dish.set_recipe(recipe)
        return period

    @abstractmethod
    def generate_meal(self, day: Day, moment: Moment) -> Meal:
        """Generate a new meal given a day and a moment.

        Args:
            day (Day): Day of the meal.
            moment (Moment): Moment of the generated meal.

        Returns:
            Meal: Meal generated.
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
        
        self.recipes = recipe_storage.get_all_recipes_with_url()
        self.recipes_seen = set()
    
    def generate_meal(self, day: Day, moment: Moment) -> Meal:
        """Generate a new meal using a unique recipe never seen.

        Args:
            day (Day): Day of the generation.
            moment (Moment): Moment of the generation.

        Returns:
            Meal: Meal generated.
        """
        print("okx")
        
        # Choose a random recipe
        chosen_recipe, _ = random.choice(self.recipes)
        
        while chosen_recipe in self.recipes_seen:
            chosen_recipe, _ = random.choice(self.recipes)
        
        # Add it to the list of seen
        self.recipes_seen.add(chosen_recipe)
        
        return Meal(moment, chosen_recipe)
        
    def reset(self):
        """TODO"""
        self.recipes_seen = set()
