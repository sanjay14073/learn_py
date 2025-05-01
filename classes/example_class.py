## Lets start writing a simple class

##define a class

class ExampleClass:
    ## define a constructor
    ## constructor is a special method that is called when an object is created
    ## in py __init__ is the constructor method
    ## also self is a reference to the current instance of the class
    ## lets say we have 2 attributes name and age
    ## now we can use a constructor to initialize these attributes

    def __init__(self,name="Prodev",age=25):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


if __name__=="__main__":
    ## create an object with default constructor
    obj=ExampleClass()
    obj.display()
    ## create an object with parameterized constructor
    obj1=ExampleClass("Prodev1",25)
    obj1.display()
