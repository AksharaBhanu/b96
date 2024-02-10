import pytest

@pytest.fixture(autouse=True, scope="session")
def pre_post2():
    print('Session start')
    yield
    print("Session ends")