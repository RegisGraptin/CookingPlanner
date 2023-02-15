import os
import pytest
import json

from fastapi.testclient import TestClient
from fastapi import status

from cookingplanner.main import app

client = TestClient(app)

fake_account = {
    "email":    'fake@example.com',
    "password": 'fakepassword',
}

fake_account_2 = {
    "email":    'fake2@example.com',
    "password": 'fakepassword',
}

@pytest.fixture(autouse=True)
def cleanup_files():
    """The database will automatically be created at the start of the script.

    We simply need to delete the test database at the end.
    """

    yield None
    
    if os.path.exists("/tmp/test.db"):
        print("Delete the database...")
        os.remove("/tmp/test.db")


def test_auth_create_account():

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

    # Try to create another account with the same email
    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )
    assert response.status_code == status.HTTP_409_CONFLICT


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

    

def test_auth_login_account():
    pass

def test_auth_create_existing_account():
    pass

def test_auth_get_user_account_info():
    pass
