
from datetime import date
from typing import List
from enum import Enum

from cookingplanner.recipe.recipe import Recipe

class Moment(Enum):
    """Moment of a day."""
    BREAKFAST   = 0
    LUNCH       = 1
    DINNER      = 2
    OTHER       = 3

class DayName(Enum):
    """Day name."""
    MONDAY      = 0 
    TUESDAY     = 1
    WEDNESDAY   = 2
    THURSDAY    = 3
    FRIDAY      = 4
    SATURDAY    = 5
    SUNDAY      = 6

class Meal:
    """Meal class."""
    
    
    def __init__(self, moment: Moment, recipe: Recipe) -> None:
        self.moment = moment
        self.dish   = recipe
        
    def __str__(self) -> str:
        return str(self.moment) + " - " + self.dish

    def get_moment(self) -> Moment:
        """Get the moment.

        Returns:
            Moment: Moment
        """
        return self.moment
    
    def get_recipe(self) -> Recipe:
        """Get the recipe

        Returns:
            Recipe: Recipe
        """
        return self.dish
    
    def set_recipe(self, recipe: Recipe):
        """Set a new recipe.

        Args:
            recipe (Recipe): New recipe.
        """
        self.dish = recipe

class Day:
    """Day class."""
    
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    def __init__(self, day_date: date, dishes: List[Meal]) -> None:
        self.date   = day_date
        self.dishes = dishes
        
    def get_day_of_the_week(self) -> str:
        """Get day of the week.

        Returns:
            str: Get the day of the week.
        """
        return Day.DAYS[self.date.weekday()]
    
    def get_dishes(self) -> List[Meal]:
        """Get the meals.

        Returns:
            List[Meal]: List of the meals.
        """
        return self.dishes
    
    def __str__(self) -> str:
        
        out = f"[{self.date}]\n"
        for moment in self.dishes:
            out += str(moment) + "\n"
        return out
    
    
class Week:
    """Week class."""
    
    def __init__(self, days: List[Day]) -> None:
        """Need to have 7 days generated

        Args:
            days (List[Day]): List of the day
        """
        self.days = days
        
    def get_days(self) -> List[Day]:
        """Get the days.

        Returns:
            List[Day]: Days of the week.
        """
        return self.days
    

    def __str__(self) -> str:
        out = ""
        for day in self.days:
            out += "-" * 20
            out += str(day) + "\n" 
        return out        