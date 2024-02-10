import pytest
@pytest.fixture(autouse=True)
def login():
    print('Login')
    yield
    print('logout')
