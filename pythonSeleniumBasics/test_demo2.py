import pytest


@pytest.mark.smoke
def test_checkDifference():
    a=5
    b=3
    assert a-2==b,"Test success. Expected and actual output  matching"