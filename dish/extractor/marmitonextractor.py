
from bs4 import BeautifulSoup
import json

class MarmitonExtractor:
    
    def _extract_total_time_duration(self):
        spans = self.content.find_all("span") 
        for span in spans:
            if span.text.startswith("Temps total:"):
                parent = span.parent
                children = parent.findChildren()
                
                self.data["duration"] = children[-1].text.replace(u'\xa0', u' ')
                return 
            
            
    def _extract_recipe(self):
        
        scripts = self.content.find_all("script")
        for script in scripts:
            if script.get('type') is not None:
                if script.get('type') == "application/ld+json":
                    content = json.loads(script.text)

                    if content.get('@type') is not None:
                        if content.get('@type') == "Recipe":
                            # print(content)

                            self.data['name'] = content['name']
                            self.data['prepTime'] = content['prepTime']
                            self.data['cookTime'] = content['cookTime']
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
        self._extract_total_time_duration()
        self._extract_recipe()
        
    def get_data(self):
        return self.data
        
        
