from typing import List

from bs4 import BeautifulSoup
import requests

from cookingplanner.scraping.scraping_extractor_strategy import ManagerExtractorStrategy


class ScrapingURL:
    """Scraping ULR class.
    
    Given a list of url, extract the recipe url present.
    """

    # List of URL to get recipe. They need to end with a '/'
    URL = [
        "https://www.marmiton.org/recettes/index/categorie/plat-principal/"
    ]

    def __init__(self, n_pages: int = 1) -> None:
        self.n_pages = n_pages
        
        self.manager_extractor = ManagerExtractorStrategy()
        
    def generate_target_url(self) -> List[str]:
        """Given the number of pages and the requested url, 
        generate the urls we want to analyze.
        
        Note: For marmiton, the page with the number 1 do not exists.
        We need to skip this one.

        Returns:
            List[str]: List of the urls we want to analyze. The returned urls
                       will finished with a '/'. 
        """
        urls = []
        
        # Create the urls given the number of pages and the requested url
        for url in ScrapingURL.URL:
            urls.append(url)
            for i in range(2, self.n_pages + 1):
                urls.append(url + str(i) + '/')
        
        return urls


    def scrap(self) -> List[str]:
        """Given a page, extract all the url present on it.

        Returns:
            List[str]: List of all the URL extracted.
        """

        # Generate the urls
        urls = []

        for target_page_url in self.generate_target_url():

            # Get the strategy for the url and extract the url
            strategy = self.manager_extractor.get(target_page_url)
            if strategy is not None:
                # Get the request
                response = requests.get(target_page_url, timeout=2)
                content = BeautifulSoup(response.content, "html.parser")
                content.prettify()
                
                # Extract the URL
                urls += strategy(content).extract_recipe_urls()
        
        return urls
