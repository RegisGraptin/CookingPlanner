
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field

from cookingplanner.models.database import Database
from cookingplanner.models.schema import Profile
from cookingplanner.routers.auth import manager

router = APIRouter()

database = Database()

class ProfileModel(BaseModel):
    """Profile model request."""
    n_persons               : int = Field(int, ge=1, le=10)
    cost                    : int = Field(int, ge=0, le=5)
    spicy                   : int = Field(int, ge=0, le=5)
    culinary_adventurousness: int = Field(int, ge=0, le=5)
    cooking_level           : int = Field(int, ge=0, le=5)
    recipe_diversity        : int = Field(int, ge=0, le=7)
    ingredient_diversity    : int = Field(int, ge=0, le=5)
    cooking_time            : int = Field(int, ge=0, le=5)
    seasonal_recipe         : bool= Field(bool)


@router.get('', status_code=status.HTTP_200_OK)
def get_user_profiles(user = Depends(manager), db_session: Session = Depends(database.create_session)):
    """Get the user profiles already defined

    Args:
        user (User, optional): Current user. Defaults to Depends(manager).
    """
    
    # Fetch the data from the user
    user_profiles = db_session.query(Profile).filter(Profile.user == user.id).all()
    
    return user_profiles

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user_profile(
    data : ProfileModel, 
    user = Depends(manager), 
    db_session: Session = Depends(database.create_session)):
    """Create a new user profile.

    Args:
        data (ProfileModel): Profile of the user
        user (User, optional): Current user. Defaults to Depends(manager).
    """

    db_user_profile = Profile(
        **data.dict(),
        user=user.id,
    )
    
    db_session.add(db_user_profile)
    db_session.commit()
    db_session.refresh(db_user_profile)

    return db_user_profile
