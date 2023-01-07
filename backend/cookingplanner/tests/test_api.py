
from fastapi.testclient import TestClient
from fastapi import status

from cookingplanner.main import app

client = TestClient(app)

def test_generate_work_week_unique_strategy():
    """Test the generation of a week with a unique recipe strategy."""
    
    # Generate a week
    response = client.get("/week/work/unique")
    assert response.status_code == status.HTTP_201_CREATED
    
    # TODO :: Verify the content of the response
    # + Each field content should not be empty/None
    
    # week_generated = response.content
    
    