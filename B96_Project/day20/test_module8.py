#excute login automatically before every test
import pytest


@pytest.fixture(autouse=True) #fixture->before every test
def login():
    print('\nlogin')

@pytest.fixture(autouse=True) #fixture + yield --> after every test
def logout():
    yield   #wait for test to complete
    print('\nlogout')


def test_create_customer():
    print('create customer')

def test_delete_customer():
    print('delete customer')

