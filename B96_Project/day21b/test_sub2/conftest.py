import pytest

@pytest.fixture(autouse=True, scope="package")
def pre_post():
    print('sub2 start')
    yield
    print("sub2 end")