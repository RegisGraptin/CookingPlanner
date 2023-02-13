from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException


from fastapi import APIRouter, Depends

router = APIRouter()

# TODO :: Change it and set it in a .env variable
SECRET = "12232040a8d9af375aab1ddad91b7db0550266799cc76c3f"

manager = LoginManager(SECRET, '/login')

# TODO :: To update it and use a User object and database
DB = {
    'users': {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
}


@manager.user_loader()
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)


@router.post('/login')  # /auth/token
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
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


