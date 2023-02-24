from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from cookingplanner.models.database import Database


Base = Database().Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
