

from cookingplanner.recipe.recipe_storage import RecipeStorage
from cookingplanner.scraping.scraping_recipe import ScrapingRecipe
from cookingplanner.scraping.scraping_url import ScrapingURL


class Scraping():
    """Scraping class.
    
    Extract new data by scraping website. First, we generate new urls with the `ScrapingURL` class.
    Then, for each extracted recipe url, we extract them with the `ScrapingRecipe` class.
    """
    
    def __init__(
        self,
        scraping_url    : ScrapingURL    = ScrapingURL(n_pages=1),
        scraping_recipe : ScrapingRecipe = ScrapingRecipe()
        ) -> None:
        """Instanciate a Scraping class.

        Args:
            scraping_url (ScrapingURL, optional): Scraping url class. Defaults to ScrapingURL(n_pages=1).
            scraping_recipe (ScrapingRecipe, optional): Scraping recipe class. Defaults to ScrapingRecipe().
        """
        
        # Define our recipe storage
        self.recipe_storage = RecipeStorage()
        
        # Define the Scraping methods
        self.scraping_url    = scraping_url
        self.scraping_recipe = scraping_recipe
    
    def scrap(self):
        """Scrap new data by generating new urls and extract the recipe from it."""
        
        # Target urls
        target_urls = self.scraping_url.scrap()
        
        for target_url in target_urls:
            
            # Check if we do not have already extract the url
            if not self.recipe_storage.exists(target_url):                
                recipe = self.scraping_recipe.scrap(target_url)
                self.recipe_storage.add(target_url, recipe)
