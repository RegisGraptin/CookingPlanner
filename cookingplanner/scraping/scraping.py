

from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scraping_recipe import ScrapingRecipe
from cookingplanner.scraping.scraping_url import ScrapingURL


class Scraping():
    """Scraping class.
    
    Extract new data by scraping website.
    """
    
    def __init__(self) -> None:
        # Define our recipe storage
        self.recipe_storage = RecipeStorage()
        
        # Define the Scraping methods
        self.scraping_url    = ScrapingURL(n_pages=1)
        self.scraping_recipe = ScrapingRecipe()
    
    def scrap(self):
        """Scrap new data by generating new urls and extract the recipe from it."""
        
        # Target urls
        target_urls = self.scraping_url.scrap()
        
        for target_url in target_urls:
            
            # Check if we do not have already extract the url
            if not self.recipe_storage.exists(target_url):                
                recipe = self.scraping_recipe.scrap(target_url)
                self.recipe_storage.add(target_url, recipe)
