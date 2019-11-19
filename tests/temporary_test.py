import pytest


#Example of passing return values to the tests.
@pytest.fixture
def temporary():
    return 1

#Names need to start with "test_"
def test_one(temporary):
    assert(temporary == 1)
