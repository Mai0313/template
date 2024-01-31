import pytest


@pytest.fixture(scope="session", autouse=True)
def get_nums() -> int:
    """This is a sample of how you can send variables to another pytest.

    TODO: This is a sample that shows how to send variables to another pytest (also test todo-to-issue action).
    """
    return 500
