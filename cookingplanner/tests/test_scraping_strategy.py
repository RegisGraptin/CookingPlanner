
import os

import requests
import pytest
import responses
from cookingplanner.recipe.recipe import Recipe

from cookingplanner.scraping.scraping_recipe import ScrapingRecipe

RESSOURCE_FOLDER = os.path.join(os.path.dirname(__file__), "./ressources/")

# URL used for mocking
URLS = {
    "recette_boeuf_bourguignon": "https://www.marmiton.org/recettes/recette_boeuf-bourguignon-rapide_19218.aspx"
}

MOCKED_URL = {}

@pytest.fixture(autouse=True)
def initialize_request():
    """Initialize testing requests by extracting them. Load them for mocking."""
    for name, url in URLS.items():
        content_page_path = os.path.join(RESSOURCE_FOLDER, name + '.html')
        if not os.path.exists(content_page_path):
            response = requests.get(url, timeout=2)
            content = response.text
            with open(content_page_path, 'w', encoding="utf-8") as file:
                file.write(content)
                
        # Load the page content
        with open(content_page_path, encoding="utf-8") as file:
            content = file.read()
            
        # Initialize url mocking
        MOCKED_URL[url] = content


def test_none_strategy():
    """Test to extract on a website where we currently do not have a strategy."""
    
    url = "https://cooking_invalid_recipe/recipe/1"
    
    scraping_recipe = ScrapingRecipe()
    recipe_extracted = scraping_recipe.scrap(url)
    
    assert recipe_extracted is None
    
    
@responses.activate
def test_marmiton_strategy():
    """Extract the recipe from a Marmiton url."""
    
    # Mocked the url request
    target_url = URLS['recette_boeuf_bourguignon']
    responses.add(responses.GET, target_url, MOCKED_URL[target_url], status=200)
    
    # Extract the content of it
    scraping_recipe = ScrapingRecipe()
    recipe_extracted = scraping_recipe.scrap(target_url)
    
    assert isinstance(recipe_extracted, Recipe)
    