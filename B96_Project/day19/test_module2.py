import pytest


class Test_C:


    def test1(self):
        print('test1 of TestC')

    @pytest.mark.skip
    def test2(self):
        print('test2 of TestC')

class Test_D:
    a = 10
    b = 5
    @pytest.mark.skip(reason="i dont want to run this")
    def test1(self):
        print('test1 of TestD')

    @pytest.mark.skipif(a>b,reason="i dont want to run this")
    def test2(self):
        print('test2 of TestD')
