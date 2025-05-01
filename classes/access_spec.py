##Here we will learn about different access specifiers in python

class Person:

    ##Protected member
    _age=None

    ##Private member
    __salary=None

    def __init__(self,name:str,age:int,salary:int)->None:
        self.name=name
        self._age=age
        self.__salary=salary

    ## Method to access protected member
    def _getAge(self)->int:
        return self._age
    
    ## Method to access private member
    def _getSalary(self)->int:
        return self.__salary
    
class Friend(Person):

    def __init__(self,p:Person)->None:
        super().__init__(p.name,p._age,p._getSalary())
            
    def getFiendDetails(self)->None:
        print(f"Friend name is {self.name}")
        print(f"Friend age is {self._age}")
        try:
            print(f"Friend salary is {self.__salary}") ## This will give error as __salary is private member of Person class
        except AttributeError as e:
            print(f"Error: {e}")


p=Person("John",25,50000)
f=Friend(p)
f.getFiendDetails()
print(f"Person name is {p.name}")
        