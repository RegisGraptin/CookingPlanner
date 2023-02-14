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

    response = client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )

    print(response)

    assert response.status_code == status.HTTP_201_CREATED
    

def test_auth_login_account():
    pass

def test_auth_create_existing_account():
    pass

def test_auth_get_user_account_info():
    pass
