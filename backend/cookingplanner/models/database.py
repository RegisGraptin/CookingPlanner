
import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from cookingplanner.config import Config

from cookingplanner.utils.singleton import SingletonMeta


# As we are using local variables, we need to be sure that the configuration is initialized
Config()

class Database(metaclass=SingletonMeta):
    def __init__(self):
        logging.info("Database creation")
        
        SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
        
        # Define the database mode
        if os.environ.get('RUN_ENV', 'prod') == 'test':
            logging.info("Database mode - testing")
            SQLALCHEMY_DATABASE_URL = "sqlite:////tmp/test.db"
        else:
            logging.info("Database mode - production")

        self.engine = create_engine(
            # ONLY for sqllite database not for other ones
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        
        self.Base = declarative_base()
    
    def get_session(self):
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        return Session()

    def generate(self):

        # Create Database Schema
        self.Base.metadata.create_all(bind=self.engine)


    def create_session(self):
        db = self.get_session()
        try:
            yield db
        finally:
            db.close()