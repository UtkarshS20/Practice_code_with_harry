class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"
u=Employee("utkarsh",30000,"sde")
v=Employee("vaibhav",20000,"sde(trainee)")
#u.name="utkarsh"
#u.salary=30000
#u.role="sde"
#v.name="vaibhav"
#v.salary=15000
#v.role="sde(trainee)"
print(u.printdetails())     #u is automatically passed in the function parameter bcz of self
print(v.printdetails())
print(u.no_of_leaves)