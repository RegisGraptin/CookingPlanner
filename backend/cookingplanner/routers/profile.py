
from fastapi import APIRouter, Depends, status

from cookingplanner.routers.auth import manager

router = APIRouter()

@router.get('', status_code=status.HTTP_200_OK)
def get_user_profiles(user = Depends(manager)):
    """Get the user profiles already defined

    Args:
        user (User, optional): Current user. Defaults to Depends(manager).
    """
    
    # TODO  :: Fetch the data from the user
    
    return 