import pytest


@pytest.fixture(scope="session", autouse=True)
def get_nums() -> int:
    """This is a sample of how you can send variables to another pytest."""
    return 500
