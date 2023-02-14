
import os

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from fastapi import APIRouter, Depends, status
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

# TODO :: To update it and use a User object and database
DB = {
    'users': {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        }
    }
}

# Dependency
def get_db():
    db = database.Database().get_session()
    try:
        yield db
    finally:
        db.close()



schema.Base.metadata.create_all(bind=database.Database().engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


@manager.user_loader()
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)


from pydantic import BaseModel

class UserRegister(BaseModel):
    email: str
    password: str

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):
    
    email = data.email
    password = data.password


    # Check email not present
    user = query_user(email)
    if user:
        raise InvalidCredentialsException
    
    # Hash password
    hashed_password = get_password_hash(password)


    # Create new user
    db_user  = User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.post('/login')  # /auth/token
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
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
