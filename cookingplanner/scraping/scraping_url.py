from typing import List

from bs4 import BeautifulSoup
import requests


class URLExtractor:
    """TODO
    """

    def extract(self):
        """Extract 
        TODO ::
        """
        recipe_links = self.content.find_all(
            "a", {"class": "recipe-card-link"})
        urls = [a.get('href') for a in recipe_links]

        self.data['urls'] = urls

    def __init__(self, content: BeautifulSoup) -> None:
        self.content = content
        self.data = {}
        self.extract()


class ScrapingURL:
    """Scraping ULR class.

    Returns:
        _type_: _description_
    """

    # List of URL to get recipe. They need to end with a '/'
    URL = [
        "https://www.marmiton.org/recettes/index/categorie/plat-principal/"
    ]

    def __init__(self, n_pages: int = 1) -> None:
        self.n_pages = n_pages
        
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

            # Get the request
            response = requests.get(target_page_url, timeout=2)
            soup = BeautifulSoup(response.content, "html.parser")
            soup.prettify()
            
            # Extract the URL
            url_extractor = URLExtractor(soup)
            urls += url_extractor.data.get('urls', [])
            

        return urls
