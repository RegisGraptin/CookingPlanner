import os
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


# @pytest.mark.parametrize('url, status_code', [
#   ('https://example.com/api/v1/endpoint', 200),
#   ('https://example.com/api/v1/invalid_endpoint', 404),
# ])
# def test_post_request_status_code(url, status_code):
#     response = requests.post(url)
#     assert response.status_code == status_code



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


def test_auth_invalid_fields():
    pass

def test_auth_get_user_account_info():
    pass
