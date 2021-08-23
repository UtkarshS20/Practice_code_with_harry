#dunder methods-methods which start and end with __ .
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    def __add__(self, other):
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary
    def __repr__(self):
        #return self.printdetails()
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
    def __str__(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"
emp1=Employee("utkarsh",30000,"sde")
#emp2=Employee("vaibhav",20000,"sde(trainee)")
#print(emp1+emp2)
#print(emp1/emp2)
print(emp1)     #str is preferred over repr
print(repr(emp1))