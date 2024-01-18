class A:
    id=0
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

    @classmethod
    def m2(cls):
        print(cls.id)

    @staticmethod
    def m3():
        print('static')

obj=A('Bhanu')
v=obj.get_name()
print(v)

A.m2()
A.m3()

print(A.id)
print(obj.name)