
import json
from bs4 import BeautifulSoup


class ExtractorStrategyInterface:
    """Extractor Strategy Interface. 
    
    Define the needed implementation for extracted content from a page.
    """
    
    def extract(self) -> dict:
        """Extract the information from a given 

        Returns:
            dict: Extracted data.
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

                    if content.get('@type') is not None:
                        if content.get('@type') == "Recipe":
                            # print(content)

                            self.data['name']      = content['name']
                            self.data['prepTime']  = content['prepTime']
                            self.data['cookTime']  = content['cookTime']
                            self.data['totalTime'] = content['totalTime']

                            self.data['recipeYield'] = content['recipeYield']

                            self.data['recipeIngredient'] = content['recipeIngredient']
                            self.data['recipeInstructions'] = content['recipeInstructions']
                            self.data['recipeCuisine'] = content['recipeCuisine']

    def __init__(self, content: BeautifulSoup) -> None:
        self.content = content
        self.data = {}

    def extract(self) -> dict:
        """Extract the information from a Marmiton page and return the extracted data.

        Returns:
            dict: Extracted data.
        """
        self._extract_total_time_duration()
        self._extract_recipe()
        return self.data
