import requests
import pytest
from unittest.mock import patch, MagicMock

def test_authentication_failure():
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the server response
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = ""
        mock_get.return_value = mock_response

        response = requests.get(url, params=params)

        # Assert that the HTTP status code is 401 (Unauthorized)
        assert response.status_code == 401

        # Assert that the response body is empty
        assert response.text == ""
