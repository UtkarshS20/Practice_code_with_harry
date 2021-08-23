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
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("great shit fam "+string)

class Programmer(Employee):
    no_of_holidays = 56
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages=alanguages

    def printprog(self):
        return f"programmer's name is {self.name} salary is {self.salary} role is {self.role} and the languagges are {self.languages}"

u=Employee("utkarsh",30000,"sde")
v=Employee("vaibhav",20000,"sde(trainee)")
j=Programmer("Jaadu",55000,"programmer",["c++"])
m=Programmer("mohit",60000,"programmer",["java"])
print(m.printprog())
print(m.no_of_holidays)
print(m.printdetails())