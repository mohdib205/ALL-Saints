'''
Abstraction
Abstraction is the concept of hiding the
implementation details and showing only
the essential features of an object or system.

Abstract Class
An abstract class is a class that cannot be
instantiated and is meant to be subclassed.
It can contain both abstract methods
(methods without implementation) and
concrete methods (methods with implementation).
It provides a common interface for its
subclasses.

Abstract Method
An abstract method is a method that is
declared in an abstract class but does
not have an implementation.
Subclasses that inherit from the abstract
class must provide their own implementation
for this method.

'''
from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4 

sq= Square(12)
print(sq.area())

print(sq.perimeter())
        






