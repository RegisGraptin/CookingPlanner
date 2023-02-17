
import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from cookingplanner.models import database
from cookingplanner.models.schema import User

router = APIRouter()


SECRET = os.environ.get("SECRET_KEY", None)

if SECRET is None:
    raise ValueError("SECRET_KEY value is not defined. Please defined it in your .env file.")

manager = LoginManager(SECRET, '/token')

database.Database()

# Dependency
def get_db():
    db = database.Database().get_session()
    try:
        yield db
    finally:
        db.close()




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)




class UserRegisterModel(BaseModel):
    """User registration model.

    Two fields are needed to register: 
    - email : email address of the user.
    - password : password of the user.
    """
    email    : EmailStr = Field()
    password : str   = Field(min_length=8)


class UserModel(BaseModel):
    """User model information."""
    email: str


EmailAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email already exists.",
    headers={"WWW-Authenticate": "Bearer"}
)

@manager.user_loader()
def get_user(email: str) -> User:
    """Get the user for the given request.

    Called by the login manager.

    Args:
        email (str): email of the user.

    Returns:
        User: Corresponding user.
    """
    # Create a database session
    db = database.Database().get_session()

    user = db.query(User).filter(User.email == email).first()

    db.close()

    return user
    


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(data: UserRegisterModel, db: Session = Depends(get_db)) -> UserModel:
    """Register a new user.

    Args:
        data (UserRegister): New user information.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Raises:
        EmailAlreadyExistsException: Account already exists with this email

    Returns:
        UserBase: Public user account information.
    """

    # Get the data
    email    = data.email
    password = data.password

    # Check that the user is not existing for the given email
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise EmailAlreadyExistsException
    
    # Hash password
    hashed_password = get_password_hash(password)

    # Create new user
    db_user  = User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserModel(email=db_user.email)


@router.post('/token')
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login the user.

    Args:
        data (OAuth2PasswordRequestForm, optional): User information. Defaults to Depends().
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Raises:
        InvalidCredentialsException: The user do not exists in the database
        InvalidCredentialsException: The user's password is not valid

    Returns:
        dict: Access token
    """
    email    = data.username
    password = data.password

    # Get the user from the database
    user = db.query(User).filter(User.email == email).first()
    
    # The user does not exist in the database
    if not user:
        raise InvalidCredentialsException
    
    # The user's password does not match with the stored password
    if not verify_password(password, user.hashed_password):
        raise InvalidCredentialsException

    # Create the access token
    access_token = manager.create_access_token(
        data={'sub': email}
    )
    
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/user')
def user(user = Depends(manager)) -> UserModel:
    """Get the user information.

    The user need to be authenticated. An access token is required.

    Args:
        user (User, optional): User from the database. Defaults to Depends(manager).

    Returns:
        UserModel: User information.
    """
    return UserModel(email=user.email)
