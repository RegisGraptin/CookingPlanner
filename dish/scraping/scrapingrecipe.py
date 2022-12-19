from bs4 import BeautifulSoup
import requests

from dish.extractor.marmitonextractor import MarmitonExtractor

class ScrapingRecipe:
    
    def __init__(self) -> None:
        pass
    
    def scrap(self, url) -> dict:
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, "html.parser")
        soup.prettify()
        
        m = MarmitonExtractor(soup)
        return m.get_data()