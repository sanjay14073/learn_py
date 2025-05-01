## Abstraction in py
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
d= Dog()
print(d.sound()) # Output: Woof!