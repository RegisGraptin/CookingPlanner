import os
import logging
import requests
import responses
import pytest

from cookingplanner.scraping.scraping_url import ScrapingURL

RESSOURCE_FOLDER = os.path.join(os.path.dirname(__file__), "./ressources/")

# Mock the urls
MOCKED_URL = {}

@pytest.fixture(autouse=True)
def get_missing_mocked_requests():
    """Initialize the requets and load them in order to mocked them later."""
    
    scraping_url = ScrapingURL(n_pages=1)
    target_urls = scraping_url.generate_target_url()
    
    for url in target_urls:
        # http://target-website.com/.../plat-principal/
        # http://target-website.com/.../plat-principal/2/
        
        # Get the possible page number
        page_number    = url.split("/")[-2]
        
        # If we do not have a number, it means that it is the first page
        if not page_number.isdigit():
            categorie_name = page_number
            response_path = os.path.join(RESSOURCE_FOLDER, categorie_name + ".html")
        else:
            categorie_name = url.split("/")[-3]
            response_path = os.path.join(RESSOURCE_FOLDER, 
                                         categorie_name + "_" + page_number + ".html")
        
        # Do the request if we do not have the response 
        if not os.path.exists(response_path):
            logging.warning("We need to load the %s. Missing %s", url, response_path)
            response = requests.get(url, timeout=2)
            content  = response.text
            with open(response_path, 'w', encoding="utf-8") as file:
                file.write(content)
                 
        # Load the request and the response
        with open(response_path, encoding="utf-8") as file:
            content = file.read()
        
        # Initialize url mocking            
        MOCKED_URL[url] = content

      
@responses.activate
def test_scraping_url():
    """Test the scraping url behavior by scrapping the recipe url on a page. 
    
    We currently have only a marmiton page. We check that we extract all the recipe on it.
    """
        
    # Set mocking response
    for url, content in MOCKED_URL.items():
        responses.add(responses.GET, url, content, status=200)
        
    scraping_url = ScrapingURL(n_pages=1)
    urls = scraping_url.scrap()
    
    assert len(urls) == 30
