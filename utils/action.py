import uuid
import requests


def create_task(payload, base_url):
    """
    Sends a PUT request to create a new task.

    Args:
        payload (dict): The payload containing task data.
        base_url (str): The base URL of the API endpoint.

    Returns:
        requests.Response: The response object containing the API response.

    """
    return requests.put(base_url + "/create-task", json=payload)


def get_task(task_id, base_url):
    """
    Sends a GET request to retrieve a task by its ID.

    Args:
        task_id (str): The ID of the task to retrieve.
        base_url (str): The base URL of the API endpoint.

    Returns:
        requests.Response: The response object containing the API response.

    """
    return requests.get(base_url + f"/get-task/{task_id}")


def new_task_payload():
    """
    Generates a new task payload.

    Returns:
        dict: The payload containing task data.

    """
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }
