
import datetime
from datetime import date

from dish.recipe.recipe_storage import RecipeStorage

from dish.generator.day import Moment
from dish.generator.day import Dish
from dish.generator.day import Day
from dish.generator.day import Week

class RecipeGenerator:
    pass


class RegularWeekGenerator:
    """RegularWeekGenerator class.
    
    Create dishes for breakfast, lunch and dinner for each day of the week.
    """
    
    REGULAR_MOMENTS = [Moment.BREAKFAST, Moment.LUNCH, Moment.DINNER]
    
    def __init__(self) -> None:
        pass
    
    def generate(self, starting_date: date) -> Week:
        days = []
        
        next_day = starting_date
        
        for _ in range(7):
            
            dishes = []
            for moment in RegularWeekGenerator.REGULAR_MOMENTS:
                dishes.append(Dish(moment, "")) 
                
            days.append(Day(next_day, dishes))
            
            next_day = next_day + datetime.timedelta(days=1)
            
        return Week(days)
            
        
            
         


class WeekGenerator:
    """Define a set of constraint given a user.
    """
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    MOMENTS = ['breakfast', 'lunch', 'dinner']
    
    def __init__(self, when: dict) -> None:
        self.when = when
        
        self.data = {}
        
        self.recipe_storage = RecipeStorage()
        
        self.generated_dish = 0
        


    def generate(self):
        # For each days of the week
        for day in WeekGenerator.DAYS:
            self.data[day] = {}
            requets_moments = self.when.get(day, [])
            
            # For each moment
            for moment in WeekGenerator.MOMENTS:
                if moment in requets_moments:
                    
                    # Generate a dish
                    url, recipe = self.recipe_storage.get_random()
                    
                    self.data[day][moment] = (url, recipe)
                    self.generated_dish += 1
                    
        return self.data
                    
                    
                
                
class DishesofTheWeek:
    """Determine the number of dish we need to have in the week.
    Based on this information generate the recipe for a given week
    """
    
    def __init__(self, week: dict) -> None:
        self.week = week
        
    def _unique_dish(self):
        """Given a week, extract the unique dishes of it."""
        
        unique_dishes = set()
        
        for day_of_week in self.week.keys():
            for moment in self.week.get(day_of_week).keys():
                url, recipe = self.week.get(day_of_week).get(moment)
                unique_dishes.add(url)
                
        print(unique_dishes)
            
        
        
    def extract(self):
        """Extract the total duration time."""
        self._unique_dish()
    

if __name__ == "__main__":
    
    when = {
        'monday':    ['breakfast', 'dinner'],
        'tuesday':   ['breakfast', 'dinner'],
        'wednesday': ['breakfast', 'dinner'],
        'thursday':  ['breakfast', 'dinner'],
        'friday':    ['breakfast', 'dinner'],
        'saturday':  ['breakfast', 'lunch', 'dinner'],
        'sunday':    ['breakfast', 'lunch', 'dinner'],
    }
    
    week = WeekGenerator(when)
    week.generate()
    
    print(week.generated_dish)
    
    dish = DishesofTheWeek(week.data)
    dish.extract()
    