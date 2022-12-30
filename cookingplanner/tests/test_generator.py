
import datetime
from cookingplanner.generator.meal import Moment, Week
from cookingplanner.generator.meal_generator import UniqueMealStrategy
from cookingplanner.generator.week_generator import AllDayWeekGenerator, GenericWeekGenerator, WorkWeekGenerator
from cookingplanner.recipe.recipe_storage import RecipeStorage


def test_generate_week_for_all_day():
    """Test the generation of a template week."""
    
    # Starting a monday
    testing_date = datetime.datetime(2022, 1, 2)
    moments = [Moment.BREAKFAST, Moment.LUNCH, Moment.DINNER]
    
    # Generate a week
    week_generator = AllDayWeekGenerator()
    generated_week = week_generator.generate(testing_date)
    
    assert len(generated_week.get_days()) == 7
    
    for day in generated_week.get_days():
        meals = day.get_meals()
        testing_moment = [meal.get_moment() for meal in meals]
        
        assert day.get_date() == testing_date
        assert len(meals) == 3    
        assert testing_moment == moments
        
        # Increase the date
        testing_date = testing_date + datetime.timedelta(days=1)
            
def test_generate_working_week():
    """Test the generation of a template week for working day.
    
    TODO :: Test depending of the day of the week if we have the good number of meals.
    """
    testing_date = datetime.datetime(2022, 1, 2)
    
    week_generator = WorkWeekGenerator()
    generated_week = week_generator.generate(testing_date)
    
    assert len(generated_week.get_days()) == 7
    
    # Check that we generate the meal with an None recipe
    all_meal = []
    for day in generated_week.get_days():
        all_meal = all_meal + day.get_meals()
    
    assert len(all_meal) == 9
    
    
def test_generate_generic_week():
    """Test the generation of a week with the generic generator.
    
    TODO :: Improve testing by checking each day.
    """
    
    testing_date = datetime.datetime(2022, 1, 2)
    
    testing_when = {
            'monday':    ['breakfast', 'dinner'],
            'tuesday':   ['breakfast'],
            'wednesday': ['breakfast', 'lunch'],
            'thursday':  ['lunch', 'dinner'],
            'friday':    [],
            'saturday':  ['dinner'],
            'sunday':    ['lunch'],
    }
    
    week_generator = GenericWeekGenerator(testing_when)
    generated_week : Week = week_generator.generate(testing_date)
    
    assert len(generated_week.get_days()) == 7
    
    all_meal = []
    for day in generated_week.get_days():
        all_meal = all_meal + day.get_meals()
    
    assert len(all_meal) == 9


def test_working_week_unique_meal_generator(fixture_recipe_storage_with_data: RecipeStorage):
    """Test the generation of meals for a working week with a unique strategy generation.
    
    Args:
        fixture_recipe_storage_with_data (RecipeStorage): Recipe storage with some data.
    """
    
    testing_date = datetime.datetime(2022, 1, 2)
    
    # Generate our template week
    generated_week = WorkWeekGenerator().generate(testing_date)
    
    # Create our unique strategy meal generator
    unique_meal_strategy = UniqueMealStrategy(fixture_recipe_storage_with_data)
    generated_week = unique_meal_strategy.generate(generated_week)
    
    # Get all the meals
    chosen_meals = []

    for day in generated_week.get_days():
        for meal in day.get_meals():
            chosen_meals.append(meal)
            assert meal is not None                    

    assert len(chosen_meals) == len(list(set(chosen_meals)))
    assert len(chosen_meals) > 0
    
