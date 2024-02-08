import pytest


#DONT use [] for parameter name if it is only one, value should be list
@pytest.mark.parametrize('un',['akash','bindu','chandana','divya'])
def test_create_customer(un):
        print('create customer',un)

#use [] for parameter name if it is more than one, value  should be tuple(best practice) in list
@pytest.mark.parametrize(['un','pw'],[['akash','a123'],('bindu','b123'),{'chandana','c123'}])
def test_create_user(un,pw):
        print('create user',un,pw)
