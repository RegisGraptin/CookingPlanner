
from datetime import date
from typing import List
from enum import Enum

class Moment(Enum):
    BREAKFAST   = 1
    LUNCH       = 2
    DINNER      = 3
    OTHER       = 4

class DayName(Enum):
    MONDAY      = 1 
    TUESDAY     = 2
    WEDNESDAY   = 3
    THURSDAY    = 4
    FRIDAY      = 5
    SATURDAY    = 6
    SUNDAY      = 7

class Dish:
    def __init__(self, moment: Moment, recipe) -> None:
        self.moment = moment
        self.dish   = recipe
        
    def __str__(self) -> str:
        return str(self.moment) + " - " + self.dish

    def get_moment(self) -> Moment:
        return self.moment
    
    def get_recipe(self):
        return self.dish
    
    def set_recipe(self, recipe):
        self.dish = recipe

class Day:
    
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    def __init__(self, date: date, dishes: List[Dish]) -> None:
        self.date   = date
        self.dishes = dishes
        
    def get_day_of_the_week(self) -> str:
        return Day.DAYS[self.date.weekday()]
    
    def get_dishes(self) -> List[Dish]:
        return self.dishes
    
    def __str__(self) -> str:
        
        out = "[{}]\n".format(self.date)
        for moment in self.dishes:
            out += str(moment) + "\n"
        return out
    
    
class Week:
    
    def __init__(self, days: List[Day]) -> None:
        """Need to have 7 days generated

        Args:
            days (List[Day]): List of the day
        """
        self.days = days
        
    def get_days(self) -> List[Day]:
        return self.days
    

    def __str__(self) -> str:
        out = ""
        for day in self.days:
            out += "-" * 20
            out += str(day) + "\n" 
        return out