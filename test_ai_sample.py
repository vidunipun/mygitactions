import pytest


def add(a, b):
    return a + b


@pytest.mark.webtest
def test_add():
    """
    Test the addition function.
    """

    assert add(3, 5) == 8
