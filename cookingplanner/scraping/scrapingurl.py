
import requests
from bs4 import BeautifulSoup
from typing import List

class URLExtractor:
    
    def extract(self):
        recipe_links = self.content.find_all("a", {"class": "recipe-card-link"})
        urls = [a.get('href') for a in recipe_links]
        
        self.data['urls'] = urls
        
    def __init__(self, content: BeautifulSoup) -> None:
        self.content = content
        self.data = {}    
        self.extract()


class ScrapingURL:
    
    URL = [
        "https://www.marmiton.org/recettes/index/categorie/plat-principal/"
    ]
    
    def __init__(self, n_pages: int = 1) -> None:
        self.n_pages = n_pages
    
    def scrap(self) -> List[str]:
        
        urls = []
        
        for i in range(1, self.n_pages + 1):
            for url in ScrapingURL.URL:
                
                # Create the url with the requested page
                uri = url + str(i)
                
                # Get the request
                response = requests.get(uri)
                soup = BeautifulSoup(response.content, "html.parser")
                soup.prettify()
                
                # Extract the URL 
                url_extractor = URLExtractor(soup)
                urls += url_extractor.data.get('urls', [])
                
        return urls
                
                
if __name__ == "__main__":
    s = ScrapingURL(n_pages=1)
    l = s.scrap()
    