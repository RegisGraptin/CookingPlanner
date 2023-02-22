
import os
import logging

from dotenv import load_dotenv

from cookingplanner.utils.singleton import SingletonMeta

class Config(metaclass=SingletonMeta):
    """Config class
    
    Define the configuration of the running app.


    OpenAPI : Default : "/openapi.json" to show else None to hide.

    """

    def __init__(self) -> None:
        self.env_name = os.environ.get('RUN_ENV', 'prod')
        self.env_file = ".env"

        self.openapi_url = "/openapi.json"

        if self.env_name == 'test':
            logging.info("Load Testing environment")
            self.env_file = ".test.env"
            
        elif self.env_name == 'prod':
            logging.info("Load Production environment")
            self.env_file = ".env"
        
        self.loaded = load_dotenv(self.env_file)

        if not os.environ.get('SHOW_OPEN_API') == "True":
            self.openapi_url = None

        # if not self.loaded or self.env_name != "prod":
        #     raise ValueError("Could not load environment variables")

    def get_openapi_url(self) -> str:
        """Get the open api url.

        Returns:
            str: Open api url if we want to show it, otherwise None.
        """
        return self.openapi_url
