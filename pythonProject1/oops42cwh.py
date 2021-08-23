class Employee:
    no_of_leaves=8
    var=8
    _protect=40
    __private=35
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

emp=Employee("utkarsh",35666,"coder")
#print(emp._protect)
#print(emp.__private)       #(name angling)-python gave it a complex so it cant be used outside
print(emp._Employee__private)