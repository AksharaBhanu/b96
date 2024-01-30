class A:
    class B:
        def test(self):
            print('test inner B')


obj=A.B()
obj.test()
