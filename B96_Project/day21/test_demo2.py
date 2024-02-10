import pytest


@pytest.fixture
def login():
    print('Login')
    yield
    print('logout')

def test_createcustomer(login):
    print('create customer')


def test_createuser(login):
    print('create user')