
import os

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

from cookingplanner.models.database import Database
from cookingplanner.models.schema import User
from cookingplanner.routers.exceptions import EmailAlreadyExistsException
from cookingplanner.routers.request_data_model import UserModel, UserRegisterModel
from cookingplanner.utils.password import PasswordManager

router = APIRouter()

SECRET = os.environ.get("SECRET_KEY", None)

if SECRET is None:
    raise ValueError("SECRET_KEY value is not defined. Please defined it in your .env file.")

manager = LoginManager(SECRET, '/token')

# Initialize the database
database = Database()


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
    db = database.get_session()

    user = db.query(User).filter(User.email == email).first()

    db.close()

    return user


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(data: UserRegisterModel, db: Session = Depends(database.create_session)) -> UserModel:
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
    hashed_password = PasswordManager().get_password_hash(password)

    # Create new user
    db_user  = User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserModel(email=db_user.email)


@router.post('/token')
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.create_session)):
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
    if not PasswordManager().verify_password(password, user.hashed_password):
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
