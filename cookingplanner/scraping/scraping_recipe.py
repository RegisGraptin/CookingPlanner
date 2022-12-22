import json
from bs4 import BeautifulSoup
import requests

class MarmitonExtractor:
    """TODO
    """

    def _extract_total_time_duration(self):
        """TODO
        """
        spans = self.content.find_all("span")
        for span in spans:
            if span.text.startswith("Temps total:"):
                parent = span.parent
                children = parent.findChildren()

                self.data["duration"] = children[-1].text.replace(
                    '\xa0', ' ')
                return

    def _extract_recipe(self):
        """TODO
        """

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

        # <script type="application/ld+json">

    def __init__(self, content: BeautifulSoup) -> None:
        self.content = content
        self.data = {}

        self.extract()

    def extract(self):
        """TODO
        """
        self._extract_total_time_duration()
        self._extract_recipe()

    def get_data(self):
        """TODO

        Returns:
            _type_: _description_
        """
        return self.data

class ScrapingRecipe:
    """TODO
    """

    def __init__(self) -> None:
        pass

    def scrap(self, url) -> dict:
        """TODO

        Args:
            url (_type_): _description_

        Returns:
            dict: _description_
        """
        response = requests.get(url, timeout=2)

        soup = BeautifulSoup(response.content, "html.parser")
        soup.prettify()

        marmiton = MarmitonExtractor(soup)
        return marmiton.get_data()
