def test_example(get_nums: int) -> None:
    """This will get variables from another pytest, `conftest.py`."""
    assert isinstance(get_nums, int)
