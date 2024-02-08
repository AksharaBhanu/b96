import pytest


@pytest.mark.run(order=1)
def test_create_customer():
    print('create customer')

@pytest.mark.run(order=3)
def test_create_user():
    print('create user')

@pytest.mark.run(order=2)
def test_delete_customer():
    print('delete customer')

@pytest.mark.run(order=4)
def test_delete_user():
    print('delete user')