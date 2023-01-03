
import datetime
from datetime import date
from typing import List

from cookingplanner.generator.meal import DayName, Meal, Moment
from cookingplanner.generator.meal import Day
from cookingplanner.generator.meal import Week

class WeekGeneratorInterface:
    """Interface for the generation of a week."""
    
    def generate(self, starting_date: date) -> Week:
        """Generate an empty week blueprint.

        Args:
            starting_date (date): Starting date of the generation.

        Returns:
            Week: Empty week generation.
        """

class AllDayWeekGenerator(WeekGeneratorInterface):
    """All Day Week Generator class.
    
    Create meal for breakfast, lunch and dinner for each day of the week.
    """
    
    REGULAR_MOMENTS = [Moment.BREAKFAST, Moment.LUNCH, Moment.DINNER]
    
    def __init__(self) -> None:
        pass
    
    def generate(self, starting_date: date) -> Week:
        days = []
        
        next_day = starting_date
        
        for _ in range(7):
            
            dishes = []
            for moment in AllDayWeekGenerator.REGULAR_MOMENTS:
                dishes.append(Meal(moment, "")) 
                
            days.append(Day(next_day, dishes))
            
            next_day = next_day + datetime.timedelta(days=1)
            
        return Week(days)

class WorkWeekGenerator(WeekGeneratorInterface):
    """Work Week Generator class.
    
    Create meal for dinner for the days of the week when we work and lunch and dinner for the weekend.
    """
    
    def __init__(self,
                 workday: List[DayName] = None,
                 weekend: List[DayName] = None):
        
        if workday is None:
            workday = [DayName.MONDAY, DayName.TUESDAY, DayName.WEDNESDAY, 
                       DayName.THURSDAY, DayName.FRIDAY]
        
        if weekend is None:
            weekend = [DayName.SATURDAY, DayName.SUNDAY]
        
        self.workday = workday
        self.weekend = weekend
        
        # Define the moment given a period of the week
        self.workday_moment = [Moment.DINNER]
        self.weekend_moment = [Moment.LUNCH, Moment.DINNER]

    def generate(self, starting_date: date) -> Week:
        days = []
        
        next_day = starting_date
        
        for _ in range(7):
            dishes = []
            
            # We have a day of work
            if DayName(next_day.weekday()) in self.workday:
                for moment in self.workday_moment:
                    dishes.append(Meal(moment, ""))
            elif DayName(next_day.weekday()) in self.weekend:
                for moment in self.weekend_moment:
                    dishes.append(Meal(moment, ""))
                
            days.append(Day(next_day, dishes))
            
            next_day = next_day + datetime.timedelta(days=1)
            
        return Week(days)

class GenericWeekGenerator(WeekGeneratorInterface):
    """Generic week generator."""
    
    def __init__(self, when: dict) -> None:
        """Given a dictionary of day and moment, generate a week.

        Args:
            when (dict): Constraints of the week generation.
            
        Example:
        when = {
            'monday':    ['breakfast', 'dinner'],
            'tuesday':   ['breakfast', 'dinner'],
            'wednesday': ['breakfast', 'dinner'],
            'thursday':  ['breakfast', 'dinner'],
            'friday':    ['breakfast', 'dinner'],
            'saturday':  ['breakfast', 'lunch', 'dinner'],
            'sunday':    ['breakfast', 'lunch', 'dinner'],
        }
        """
        super().__init__()
        
        self.when = when
        
        # Be sure that all the day are defined.
        if set(self.when.keys()) != set(Day.DAYS):
            raise Exception("Invalid dictionary value, missing day.")
        

    def generate(self, starting_date: date) -> Week:
        """Given a starting date, generate the week template.

        Args:
            starting_date (date): Starting date.

        Returns:
            Week: Generated week.
        """
        days = []
        next_day = starting_date
        
        for _ in range(7):
            # Get the day name
            name_of_day = next_day.strftime('%A').lower()
            
            dishes = []
            
            if self.when.get(name_of_day) is not None:
                moments = self.when.get(name_of_day)
                for moment in moments:
                    dishes.append(Meal(moment, ""))
            
            days.append(Day(next_day, dishes))
            next_day = next_day + datetime.timedelta(days=1)
        
        return Week(days)
    

@DeprecationWarning    
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
                url, _ = self.week.get(day_of_week).get(moment)
                unique_dishes.add(url)
            
    def extract(self):
        """Extract the total duration time."""
        self._unique_dish()
    

if __name__ == "__main__":
    
    when_week = {
        'monday':    ['breakfast', 'dinner'],
        'tuesday':   ['breakfast', 'dinner'],
        'wednesday': ['breakfast', 'dinner'],
        'thursday':  ['breakfast', 'dinner'],
        'friday':    ['breakfast', 'dinner'],
        'saturday':  ['breakfast', 'lunch', 'dinner'],
        'sunday':    ['breakfast', 'lunch', 'dinner'],
    }
    
    # week = WeekGenerator(when)
    # week.generate()
    
    # print(week.generated_dish)
    
    # dish = DishesofTheWeek(week.data)
    # dish.extract()
    