import requests
import pytest

from utils.action import create_task, get_task, new_task_payload
from utils.extract_json_data import extract_json_data


@pytest.mark.api
def test_status_code(base_url):
    """
    Test case to verify the status code of an API endpoint.

    This test sends a GET request to the specified base_url and checks if the
    response status code is 200 (OK).

    Args:
        base_url (str): The URL of the API endpoint to be tested.

    Raises:
        AssertionError: If the response status code not 200.
    """
    response = requests.get(base_url)
    assert response.status_code == 200, "Status Code does not matches"


@pytest.mark.api
def test_response_time(base_url):
    """
      Test case to verify the response time of an API endpoint.

      This test sends a GET request to the specified base_url and checks if the
      response time is less than 1 second.

      Args:
          base_url (str): The URL of the API endpoint to be tested.

      Raises:
          AssertionError: If the response time exceeds 1 second.
      """
    response = requests.get(base_url)
    assert response.elapsed.total_seconds() < 1, "Response time is too long"


@pytest.mark.api
def test_response_data(base_url):
    """
    Test case to validate the response data of the API.

    This test sends a GET request to the specified `base_url` and checks if the response
    is in JSON format and matches the expected data.

    Args:
        base_url (str): The base URL of the API.

    Raises:
        AssertionError: If the response is not in JSON format or the data does not match
            the expected data.
    """
    response = requests.get(base_url)
    print(response.json())
    expected_data = extract_json_data("expected_data")
    print(expected_data)
    assert response.headers["Content-Type"] == "application/json", "Response is not in JSON format"
    assert expected_data == response.json(), "Response data is missing expected key"


@pytest.mark.api
def test_create_task(base_url):
    """
    Test case to verify that a task can be successfully created through the API.

    This test performs the following steps:
    1. Create a new task using the `create_task` API.
    2. Asserts that the task creation is successful by checking the status code.
    3. Retrieve the created task using the `get_task` API.
    4. Verifies that the retrieved task has the same content and user ID as the one created.

    Args:
        base_url (str): The URL of the API endpoint to be tested.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    payload = new_task_payload()
    create_task_response = create_task(payload, base_url)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id, base_url)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


