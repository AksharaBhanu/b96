class A:

    def __init__(self):
        self.name='bhanu'

    def get_name(self):
        return self.name

    @property               #getter method which do not take any input arg but only returns a value
    def myname(self):
        return self.name



obj=A()
v1=obj.name  #f
print(v1)

v2=obj.get_name()  #m
print(v2)

v3=obj.myname #p
print(v3)

print(obj.myname)