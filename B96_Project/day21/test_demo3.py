import pytest


@pytest.fixture(autouse=True)
def login():
    print('Login')
    yield
    print('logout')

def test_createcustomer():
    print('create customer')


def test_createuser():
    print('create user')