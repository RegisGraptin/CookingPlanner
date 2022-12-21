
from cookingplanner.scraping.scrapingurl import ScrapingURL


def test_scraping_url():
    scrapingURL = ScrapingURL(n_pages=1)
    urls = scrapingURL.scrap()
    
    assert len(urls) > 0
