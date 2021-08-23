#from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod      #for python 3.4 and later
#class Shape(metaclass=ABCMeta):
class Shape(ABC):
    @abstractmethod
    def p_area(self):
        return 0
class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
    def p_area(self):
        return self.length*self.breadth

rect1=Rectangle()
print(rect1.p_area())
#tryobj=Shape()