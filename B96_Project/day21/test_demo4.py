import pytest


@pytest.fixture(autouse=True,params=['bhanu','ravi','surya'])
def login(request):
    un=request.param
    print('Login as',un)
    yield
    print('logout')


def test_createcustomer(un):
    print('create customer',un)
