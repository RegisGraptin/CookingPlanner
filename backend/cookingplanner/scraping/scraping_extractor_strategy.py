
import json
from typing import List
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from cookingplanner.recipe.recipe import Recipe
from cookingplanner.utils.singleton import SingletonMeta


class ExtractorStrategyInterface:
    """Extractor Strategy Interface. 
    
    Define the needed implementation for extracted content from a page.
    """
    
    def extract_recipe(self) -> Recipe:
        """Extract the information from a given 

        Returns:
            dict: Extracted data.
        """

    def extract_recipe_urls(self) -> List[str]:
        """Given a page, extract the urls recipe

        Returns:
            List[str]: List of recipe urls extracted.
        """
        
class MarmitonExtractorStrategy(ExtractorStrategyInterface):
    """Extract information from a marmiton page.
    
    The extracted information are normalize into a dictionary variable.
    """

    def _extract_total_time_duration(self) -> None:
        """Extract the total time of the recipe."""
        spans = self.content.find_all("span")
        for span in spans:
            if span.text.startswith("Temps total:"):
                parent = span.parent
                children = parent.findChildren()

                self.data["duration"] = children[-1].text.replace(
                    '\xa0', ' ')
                return

    def _extract_recipe(self) -> None:
        """Extract the recipe information on the page."""
        scripts = self.content.find_all("script")
        for script in scripts:
            if script.get('type') is not None:
                if script.get('type') == "application/ld+json":
                    content = json.loads(script.text)

                    if content.get('@type') is not None and content.get('@type') == "Recipe":
                
                        self.data['name']      = content['name']
                        self.data['prepTime']  = content['prepTime']
                        self.data['cookTime']  = content['cookTime']
                        self.data['totalTime'] = content['totalTime']

                        self.data['recipeYield'] = content['recipeYield']

                        self.data['recipeIngredient'] = content['recipeIngredient']
                        
                        self.data['recipeCuisine'] = content['recipeCuisine']
                        
                        # Format [{"@type": type, "text": text}, ...]
                        # {"@type": "HowToStep", "text": "Hacher les oignons. Peler l'ail."} 
                        self.data['recipeInstructions'] = []
                        for recipe_instruction in content['recipeInstructions']:
                            self.data['recipeInstructions'].append(
                                {'type': recipe_instruction.get('@type'), 'text': recipe_instruction.get('text')}
                            )
                            

    def extract_recipe(self) -> dict:
        """Extract the information from a Marmiton page and return the extracted data.

        Returns:
            dict: Extracted data.
        """
        self._extract_total_time_duration()
        self._extract_recipe()
        return Recipe(self.data, self.source_url)
    
    def extract_recipe_urls(self) -> List[str]:
        """Extract the recipe urls present on the page.

        Returns:
            List[str]: List of the urls extracted.
        """
        
        recipe_links = self.content.find_all(
            "a", {"class": "recipe-card-link"})
        urls = [a.get('href') for a in recipe_links]

        # Save the url
        self.data['urls'] = urls
        
        return urls
    
    def __init__(self, content: BeautifulSoup, source_url: str) -> None:
        self.content = content
        self.source_url = source_url
        self.data = {}

class ManagerExtractorStrategy(metaclass=SingletonMeta):
    """Manager Extractor Strategy class.
    
    Given a url, get the associated class allowing the extraction. 
    This implementation allows the modularity of the extraction 
    on new website by simply adding a new url domain and the 
    corresponding `ExtractorStrategyInterface` class.

    Args:
        metaclass (SingletonMeta, optional): Singleton class. Defaults to SingletonMeta.
    """
    
    def __init__(self) -> None:
        self.strategies = {
            urlparse("https://www.marmiton.org").hostname: MarmitonExtractorStrategy
        }
        
    def get(self, url: str) -> ExtractorStrategyInterface:
        """Given a url, return the associated extractor strategy.

        Args:
            url (str): Url we want to scrap.

        Returns:
            ExtractorStrategyInterface: Strategy for the extraction.
        """
        domain_request = urlparse(url).hostname
        return self.strategies.get(domain_request)
