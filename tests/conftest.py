import pytest


@pytest.fixture()
def base_url():
    """
    Pytest fixture that provides the base URL of the API endpoint.

    Returns:
        str: The base URL of the API endpoint.
    """
    return "https://todo.pixegami.io/"



