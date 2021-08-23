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

u=Employee("utkarsh",30000,"sde")
v=Employee("vaibhav",20000,"sde(trainee)")
u.change_leaves(34)
print(u.no_of_leaves)