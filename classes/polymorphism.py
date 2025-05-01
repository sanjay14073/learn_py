## Example of polymorphism in python

## Function overloading
## 2 add methods with different number of arguments
def add(a,b,c=0):
    return a+b+c

##Now function overriding

class Parent:
    def addNumbers(self,a:str,b:str)->int:
        print("Parent class")
        return int(a)+int(b)

class Child(Parent):
    def addNumbers(self,a:float,b:float)->float:
        print("Child class")
        return a+b
    


## Testing overloading
print(add(1,2))
print(add(1,2,3))

## Testing overiding
c=Child()
super(Child, c).addNumbers("1", "2")  # Calls Parent's method explicitly
c.addNumbers(1.0,2.0)

## Another advanced way of dealing with polymorphism 

from functools import singledispatch

@singledispatch
def process(value):
    print("Default processing:", value)

@process.register(int)
def _(value):
    print("Processing an integer:", value)

@process.register(str)
def _(value):
    print("Processing a string:", value)

@process.register(float)
def _(value):
    print("Processing a float:", value)

# Test
process(10)       # Processing an integer: 10
process("hello")  # Processing a string: hello
process(3.14)     # Processing a float: 3.14
process([1, 2, 3])# Default processing: [1, 2, 3]
