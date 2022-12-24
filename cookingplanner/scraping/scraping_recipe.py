from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from cookingplanner.recipe.recipe import Recipe
from cookingplanner.scraping.scraping_extractor_strategy import \
    MarmitonExtractorStrategy


class ScrapingRecipe:
    """Scraping a page with a recipe.
    
    Based on the given url, a specific strategy will be apply in order 
    to extract correctly the information on it.
    """

    def __init__(self) -> None:
        """Initialize the strategies based on the domain name."""
        
        self.strategies = {
            urlparse("https://www.marmiton.org").hostname: MarmitonExtractorStrategy
        }

    def scrap(self, url: str) -> Recipe:
        """Given a url, extract the recipe from it.

        Args:
            url (str): url where we want to extract the recipe.

        Returns:
            Recipe: Recipe extracted.
        """
        
        # Verify that the extracted strategy exists
        domain_request = urlparse(url).hostname
        strategy = self.strategies.get(domain_request)
        
        if strategy is None:
            return None
        
        # Get the content of the page
        response = requests.get(url, timeout=2)
        content = BeautifulSoup(response.content, "html.parser")
        content.prettify()

        # Given the strategy, extract the recipe
        return Recipe(strategy(content).extract())
