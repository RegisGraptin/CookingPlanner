
import os

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from cookingplanner.models.schema import User

from cookingplanner.models import database, schema


router = APIRouter()


# TODO :: Change it and set it in a .env variable
SECRET = os.environ.get("SECRET_KEY", None)

if SECRET is None:
    raise ValueError("SECRET_KEY value is not defined. Please defined it in your .env file.")

manager = LoginManager(SECRET, '/login')

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


from pydantic import BaseModel, EmailStr, Field

class UserRegisterModel(BaseModel):
    """User registration model.

    Two fields are needed to register: 
    - email : email address of the user.
    - password : password of the user.
    """
    email    : EmailStr = Field()
    password : str   = Field(min_length=8)


class UserBase(BaseModel):
    email: str


EmailAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email already exists.",
    headers={"WWW-Authenticate": "Bearer"}
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(data: UserRegisterModel, db: Session = Depends(get_db)) -> UserBase:
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

    return UserBase(email=db_user.email)


@router.post('/token')  # /auth/token
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    email = data.username
    password = data.password

    user = db.query(User).filter(User.email == email).first()
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    if not verify_password(password, user.hashed_password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/user')
def user(user=Depends(manager)):
    """
    Need token in the `Authorization` as follow:
    Bearer <token>
    """
    return {'user': user}
