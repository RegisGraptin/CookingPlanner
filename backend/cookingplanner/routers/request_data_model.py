
from pydantic import BaseModel, EmailStr, Field

class UserRegisterModel(BaseModel):
    """User registration model.

    Two fields are needed to register: 
    - email : email address of the user.
    - password : password of the user.
    """
    email    : EmailStr = Field()
    password : str      = Field(min_length=8)


class UserLoginModel(BaseModel):
    """User Login Model.
    
    Two fields are defined:
    - username: email address.
    - password: password of the user.

    Note: here, we choose the username instead of the email name because of the OAuth 2 standard.
    """
    username : EmailStr = Field()
    password : str      = Field(min_length=8)

class UserModel(BaseModel):
    """User model information."""
    email: str
