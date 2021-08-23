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
    @classmethod
    def from_str(cls,string):
        #a=string.split("-")     #spilt() splits the string using the character passed through it and stores them in a list
        #return cls(a[0],a[1],a[2])
        return cls(*string.split("-"))
u=Employee("utkarsh",30000,"sde")
v=Employee("vaibhav",20000,"sde(trainee)")
m=Employee.from_str("mohit-15000-sde(junior)")
#u.change_leaves(34)
#print(u.no_of_leaves)
print(m.salary)