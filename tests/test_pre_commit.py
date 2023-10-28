def test_example(get_variables):
    """This will get variables from another pytest, `conftest.py`."""
    assert isinstance(get_variables, int)
