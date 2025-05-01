## Example for inheritance in python

class Animal:
    def __init__(self,name):
        self.name=name
        print(f"Base class constructor")

    def display(self):
        print(f"Animal name is {self.name}")
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        print(f"Derived class constructor")
    
    def display(self):
        super().display()
        print(f"Dog breed is {self.breed}")

if __name__=="__main__":
    ## create an object of base class
    obj=Animal("Dog")
    obj.display()
    ## create an object of derived class
    obj1=Dog("Dog","Labrador")
    obj1.display()
