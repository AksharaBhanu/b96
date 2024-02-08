import pytest
# we have 2 tests, delete customer & create customer
#default execution order --> delete customer & then create customer
#how do u execute delete customer after executing create customer?--> order
#how do u execute delete customer after create customer is PASSED--> dependency


@pytest.mark.dependency
def test_create_customer():
    print('create customer')
    assert False

@pytest.mark.dependency(depends=["test_create_customer"])
def test_delete_customer():
    print('delete customer')
    assert False



