
import os
import logging

from dotenv import load_dotenv

from cookingplanner.utils.singleton import SingletonMeta

class Config(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.env_name = os.environ.get('RUN_ENV', 'prod')
        self.env_file = ".env"

        if self.env_name == 'test':
            logging.info("Load Testing environment")
            self.env_file = ".test.env"
            
        elif self.env_name == 'prod':
            logging.info("Load Production environment")
            self.env_file = ".env"
        
        self.loaded = load_dotenv(self.env_file)

        if not self.loaded:
            raise ValueError("Could not load environment variabls")