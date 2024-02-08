import pytest

@pytest.mark.smoke
@pytest.mark.customer
def test_create_c():
    print('create customer')

@pytest.mark.reg
@pytest.mark.customer
def test_e_customer():
    print('edit customer')

@pytest.mark.reg
@pytest.mark.customer
def test_del_customer():
    print('delete customer')

@pytest.mark.user
@pytest.mark.smoke
def test_c_user():
    print('create user')

@pytest.mark.reg
@pytest.mark.user
def test_edit_user():
    print('edit user')

@pytest.mark.reg
@pytest.mark.user
def test_delete_user():
    print('delete user')

@pytest.mark.product
@pytest.mark.smoke
def test_create_p():
    print('create product')

@pytest.mark.reg
@pytest.mark.product
def test_edit_product():
    print('edit product')

@pytest.mark.reg
@pytest.mark.product
def test_delete_product():
    print('delete product')