import pytest
# we have 2 tests, delete customer & create customer
#default execution order --> delete customer & then create customer
#how do u execute delete customer after executing create customer?--> order
#how do u execute delete customer after create customer is PASSED--> dependency

class TestA:

    @pytest.mark.dependency(name='cc')
    def test_create_customer(self):
        print('create customer')
        assert False

    @pytest.mark.dependency(depends=["cc"])
    def test_delete_customer(self):
        print('delete customer')
        assert False



