import pytest

@pytest.fixture(autouse=True, scope="package")
def pre_post():
    print('sub1 start')
    yield
    print("sub1 end")