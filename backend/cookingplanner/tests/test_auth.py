import time
import pytest
import json

from fastapi.testclient import TestClient
from fastapi import status

from cookingplanner.main import app
from cookingplanner.models.database import Database

client = TestClient(app)

fake_account = {
    "email":    'fake@example.com',
    "password": 'fakepassword',
}

fake_account_2 = {
    "email":    'fake2@example.com',
    "password": 'fakepassword',
}

@pytest.fixture(autouse=True, scope='function')
def cleanup_files():
    """The database will automatically be created at the start of the script.

    We simply need to delete the test database at the end.
    """
    Database().generate()
    yield None
    Database().Base().metadata.drop_all(bind=Database().engine)


def test_auth_create_account():
    """Test the account creation request with an email and a password."""

    # Create a new account
    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    assert response.status_code == status.HTTP_201_CREATED

    content = json.loads(response.content)

    assert content.get('email')          == fake_account.get('email')
    assert content.get('password', None) == None
    assert len(content.keys())           == 1

    # Create another account with a new email
    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account_2),
    )

    assert response.status_code == status.HTTP_201_CREATED

    content = json.loads(response.content)

    assert content.get('email')          == fake_account_2.get('email')
    assert content.get('password', None) == None
    assert len(content.keys())           == 1

@pytest.mark.parametrize("email, password", [
    ("invalid_email", "password"),
    ("valid@email.com", ""),
    ("v@test_com", "random_password"),
    ("v@test", "random_password"),
    ("v-test@.com", "random_password"),
    ("valid@email.com", "short"),
    ("valid@email.com", "shor12-"),
])
def test_auth_register_with_invalid_fields(email: str, password: str):
    """Test to create a new account with invalid fields

    Args:
        email (str): Testing email address.
        password (str): Testing password.
    """
    
    # Try to create a new user account
    response = client.post(
        '/auth/register', 
        content=json.dumps({
            "email"   : email,
            "password": password
        }),
    )

    assert response.status_code != status.HTTP_201_CREATED

def test_auth_login_account():
    """Get authentication tokens by logging in the user"""

    # Create a new account
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    # Login the user
    response = client.post(
        '/auth/token',
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        },
        
    )

    assert response.status_code == status.HTTP_200_OK

    # Get the access token
    data = json.loads(response.content)

    assert data.get("access_token") is not None
    assert data.get("token_type")   is not None
    assert data.get("token_type") == "bearer"
    assert len(data.get("access_token")) > 50


def test_auth_login_with_non_existing_account():
    """Try to login with a non existing account."""

    response = client.post(
        '/auth/token', 
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_auth_login_wrong_password():
    """Try to login with a wrong password"""

    # Create a new account
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    # Login the user
    access_response = client.post(
        '/auth/token',
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password') + "_error",
        },
        
    )

    assert access_response.status_code == status.HTTP_401_UNAUTHORIZED

def test_auth_create_existing_account():
    """Verify that we cannot create a new account with the same email address."""

    # The first account creation should works
    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    assert response.status_code == status.HTTP_201_CREATED

    # Try to create another account with the same email
    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )
    assert response.status_code == status.HTTP_409_CONFLICT

def test_auth_get_user_account_info():
    """Create a new user account, login and get the user information"""
    
    # Create a new account
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    # Login the user
    access_response = client.post(
        '/auth/token',
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        },
        
    )

    data = json.loads(access_response.content)
    
    token = data.get('access_token')

    headers = {"Authorization": f"Bearer {token}"}

    # Get user information
    response = client.get(
        '/auth/user',
        headers = headers
    )

    assert response.status_code == status.HTTP_200_OK

    user = json.loads(response.content)
    
    assert user is not None
    assert user.get('email') == "fake@example.com"
    assert user.get('hashed_password') is None

def test_auth_get_user_without_token():
    # Create a new account
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )
    
    response = client.get(
        '/auth/user'
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    token = "invalid_token"

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get(
        '/auth/user',
        headers = headers
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmYWtlQGV4YW1wbGUuY29tIiwiZXhwIjoxNjc2NjcwNzA4fQ.eyJzdWIiOiJmYWtlQGV4YW1wbGUuY29tIiwiZXhwIjoxNjc2NjcwNzA4fQ"

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get(
        '/auth/user',
        headers = headers
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth_double_login_token_validity():
    """Check that the token changed when we login a new time.
    And check that we can login with both token as the access token should not change between the two requests.
    """
    
    # Create a new account
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    # Login the user
    access_response = client.post(
        '/auth/token',
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        },   
    )

    # Wait a second to force the change of the other auth token
    time.sleep(1)

    data = json.loads(access_response.content)
    first_token = data.get('access_token')


    # Login the user
    access_response_2 = client.post(
        '/auth/token',
        data={
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        },   
    )

    data = json.loads(access_response_2.content)
    second_token = data.get('access_token')

    assert first_token != second_token

    
    headers = {"Authorization": f"Bearer {first_token}"}

    # Get user information
    response = client.get(
        '/auth/user',
        headers = headers
    )

    assert response.status_code == status.HTTP_200_OK


    headers = {"Authorization": f"Bearer {second_token}"}

    # Get user information
    response = client.get(
        '/auth/user',
        headers = headers
    )

    assert response.status_code == status.HTTP_200_OK
