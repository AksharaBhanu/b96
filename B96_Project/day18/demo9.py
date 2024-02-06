#Page Object model -- design pattern
#for every page we create class which contains elements and methods
#number of POM class will be same as number of webpages
#we do not run POM class directly
#POM class is used only for storing elements and methods -- repository class
# to execute we create another class --Test class
#number of TC will be same as number of manual test cases
#we use encapsulation --3 steps 1 declaration 2 initailization 3 utilization
class A:
    __name=None #declartion

    def set_name(self,name):
     self.__name=name #initailization

    def get_name(self):
        return self.__name #utilization


obj=A();
obj.set_name('Bhanu')
print(obj.get_name())
