
import json
import pytest
from fastapi import status
from fastapi.testclient import TestClient

from cookingplanner.main import app
from cookingplanner.models.database import Database

client = TestClient(app)

@pytest.fixture(autouse=True, scope='function')
def cleanup_files():
    """The database will automatically be created at the start of the script.

    We simply need to delete the test database at the end.
    """
    Database().generate()
    yield None
    Database().Base().metadata.drop_all(bind=Database().engine)

fake_account = {
    "email":    'fake@example.com',
    "password": 'fakepassword',
}


fake_profile = {
    "n_persons"                : 10,
    "cost"                     : 0,
    "spicy"                    : 2,
    "culinary_adventurousness" : 2,
    "cooking_level"            : 2,
    "recipe_diversity"         : 2,
    "ingredient_diversity"     : 2,
    "cooking_time"             : 0,
    "seasonal_recipe"          : True,
}

@pytest.fixture
def access_token():
    """Get an access token from a new user created for this specific test.

    Yields:
        str: Access token of the user created.
    """
    client.post(
        '/auth/register', 
        content=json.dumps(fake_account),
    )
    response = client.post(
        '/auth/login',
        content=json.dumps({
            "username": fake_account.get('email'), 
            "password": fake_account.get('password'),
        }),
    )
    token = json.loads(response.content).get('access_token')
    
    yield token

    # TODO :: Delete the user account


def test_create_profile(access_token: str):
    """Create a new profil for a user.

    Args:
        access_token (str): Access token of a user.
    """

    # Create a new profile
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post(
        '/profile/',
        content=json.dumps(fake_profile),
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    # Check the matching between the request and the created one
    profile_created = json.loads(response.content)
    for key in fake_profile:
        assert profile_created.get(key) is not None
        assert fake_profile.get(key) == profile_created.get(key)

    # Get the user profile list from the user
    response = client.get(
        '/profile/',
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK

    profiles = json.loads(response.content)
    assert len(profiles) == 1
    
